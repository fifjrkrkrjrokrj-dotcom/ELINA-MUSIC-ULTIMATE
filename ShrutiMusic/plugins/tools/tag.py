import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ParseMode
from pyrogram.errors import FloodWait
import random
import re

from ShrutiMusic import app

SPAM_CHATS = []

def clean_text(text):
    if not text:
        return ""
    return re.sub(r'([_*\`\[])', r'\\\1', text)

async def is_admin(chat_id, user_id):
    admin_ids = [
        admin.user.id
        async for admin in app.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        )
    ]
    return user_id in admin_ids

async def process_members(chat_id, members, text=None, replied=None, is_all=True):
    tagged_members = 0
    batch = 0
    usernum = 0
    lines = []
    total = len(members)

    for member in members:
        if chat_id not in SPAM_CHATS:
            break
        if member.user.is_deleted or member.user.is_bot:
            continue

        tagged_members += 1
        usernum += 1
        name = member.user.first_name or "User"
        lines.append(f"\u25c8 <a href=\"tg://user?id={member.user.id}\">{clean_text(name)}</a>")

        if usernum == 5:
            batch += 1
            header = f"{text}\n\n" if text else ""
            body = "\n".join(lines)
            footer = f"\n\n\U0001f3c6 TAGGED {tagged_members} USERS\n\U0001f552 Batch {batch}/{((total + 4) // 5)}"
            msg = header + body + footer
            try:
                if replied:
                    await replied.reply_text(msg, disable_web_page_preview=True, parse_mode=ParseMode.HTML)
                else:
                    await app.send_message(chat_id, msg, disable_web_page_preview=True, parse_mode=ParseMode.HTML)
            except FloodWait as e:
                await asyncio.sleep(e.value + 1)
            except Exception:
                pass
            await asyncio.sleep(2)
            usernum = 0
            lines = []

    if usernum > 0 and chat_id in SPAM_CHATS:
        batch += 1
        header = f"{text}\n\n" if text else ""
        body = "\n".join(lines)
        footer = f"\n\n\U0001f3c6 TAGGED {tagged_members} USERS\n\U0001f552 Batch {batch}/{((total + 4) // 5)}"
        msg = header + body + footer
        try:
            if replied:
                await replied.reply_text(msg, disable_web_page_preview=True, parse_mode=ParseMode.HTML)
            else:
                await app.send_message(chat_id, msg, disable_web_page_preview=True, parse_mode=ParseMode.HTML)
        except Exception:
            pass

    return tagged_members

@app.on_message(
    filters.command(["all", "allmention", "mentionall", "tagall"], prefixes=["/", "@"])
)
async def tag_all_users(_, message):
    admin = await is_admin(message.chat.id, message.from_user.id)
    if not admin:
        return await message.reply_text("Only admins can use this command.")

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "Tagging process is already running. Use /cancel to stop it."
        )

    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        return await message.reply_text(
            "Give some text to tag all, like: `/all Hi Friends`"
        )

    try:
        members = []
        async for m in app.get_chat_members(message.chat.id):
            members.append(m)

        total_members = len(members)
        SPAM_CHATS.append(message.chat.id)

        text = None
        if not replied:
            text = message.text.split(None, 1)[1] if len(message.command) > 1 else None
        elif replied and replied.text:
            text = replied.text

        tagged_count = await process_members(
            message.chat.id,
            members,
            text=text,
            replied=replied,
            is_all=True
        )

        summary = f"\u2705 Tagging completed!\n\nTotal members: {total_members}\nTagged members: {tagged_count}"
        await app.send_message(message.chat.id, summary)

    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        await app.send_message(message.chat.id, f"An error occurred: {str(e)}")
    finally:
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass

@app.on_message(
    filters.command(["admintag", "adminmention", "admins", "report"], prefixes=["/", "@"])
)
async def tag_all_admins(_, message):
    if not message.from_user:
        return

    admin = await is_admin(message.chat.id, message.from_user.id)
    if not admin:
        return await message.reply_text("Only admins can use this command.")

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "Tagging process is already running. Use /cancel to stop it."
        )

    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        return await message.reply_text(
            "Give some text to tag admins, like: `/admins Hi Friends`"
        )

    try:
        members = []
        async for m in app.get_chat_members(
            message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            members.append(m)

        total_admins = len(members)
        SPAM_CHATS.append(message.chat.id)

        text = None
        if not replied:
            text = message.text.split(None, 1)[1] if len(message.command) > 1 else None
        elif replied and replied.text:
            text = replied.text

        tagged_count = await process_members(
            message.chat.id,
            members,
            text=text,
            replied=replied,
            is_all=False
        )

        summary = f"\u2705 Admin tagging completed!\n\nTotal admins: {total_admins}\nTagged admins: {tagged_count}"
        await app.send_message(message.chat.id, summary)

    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        await app.send_message(message.chat.id, f"An error occurred: {str(e)}")
    finally:
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass

@app.on_message(
    filters.command(
        [
            "stopmention",
            "cancel",
            "cancelmention",
            "offmention",
            "mentionoff",
            "cancelall",
        ],
        prefixes=["/", "@"],
    )
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    admin = await is_admin(chat_id, message.from_user.id)
    if not admin:
        return await message.reply_text("Only admins can use this command.")

    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("Tagging process successfully stopped!")
    else:
        return await message.reply_text("No tagging process is currently running!")

MODULE = "T\u1ea1g\u1ea1ll"
HELP = """
@all or /all | /tagall or @tagall | /mentionall or @mentionall [text] or [reply to any message] - Tag all users in your group with bullet mentions and batch summary

/admintag or @admintag | /adminmention or @adminmention | /admins or @admins [text] or [reply to any message] - Tag all admins in your group

/stopmention or @stopmention | /cancel or @cancel | /offmention or @offmention | /mentionoff or @mentionoff | /cancelall or @cancelall - Stop any running tagging process

Note:

1. These commands can only be used by admins
2. The bot must be an admin in your group
3. Users are tagged with clean bullet-style mentions
4. Each batch shows tagged count and batch number
5. After completion, you'll get a summary with counts
"""

