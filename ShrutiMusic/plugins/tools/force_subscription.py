import asyncio

from pyrogram import Client, filters, enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    ChatPermissions,
)
from pymongo import MongoClient
from ShrutiMusic import app
from ShrutiMusic.misc import SUDOERS
from config import MONGO_DB_URI, styled_button
from pyrogram.errors import (
    ChatAdminRequired,
    UserNotParticipant,
    FloodWait,
)

fsubdb = MongoClient(MONGO_DB_URI)
forcesub_collection = fsubdb.status_db.status


# ─── Helper: get join button markup ──────────────────────────────────────────
def _fsub_markup(channel_url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                styled_button(
                    "✅ Join Channel",
                    url=channel_url,
                    style=enums.ButtonStyle.SUCCESS,
                )
            ],
            [
                styled_button(
                    "🔄 I Joined — Check Again",
                    callback_data="fsub_check",
                    style=enums.ButtonStyle.PRIMARY,
                )
            ],
        ]
    )


# ─── /fsub command ────────────────────────────────────────────────────────────
@app.on_message(filters.command(["fsub", "forcesub"]) & filters.group)
async def set_forcesub(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        member = await client.get_chat_member(chat_id, user_id)
        is_admin = member.status in [
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR,
        ]
    except Exception:
        is_admin = False

    if not (is_admin or user_id in SUDOERS):
        return await message.reply_text(
            "❌ <b>Only group admins or sudoers can use this command.</b>"
        )

    # Disable
    if len(message.command) == 2 and message.command[1].lower() in ["off", "disable"]:
        forcesub_collection.delete_one({"chat_id": chat_id})
        return await message.reply_text(
            "✅ <b>Force subscription has been disabled for this group.</b>"
        )

    if len(message.command) != 2:
        return await message.reply_text(
            "<blockquote>"
            "🔒 <b>Force Subscription</b>\n\n"
            "📌 Usage:\n"
            "• <code>/fsub @channel_username</code>\n"
            "• <code>/fsub -100xxxxxxxxx</code> (numeric ID)\n"
            "• <code>/fsub off</code> — disable"
            "</blockquote>"
        )

    channel_input = message.command[1]

    try:
        channel_info = await client.get_chat(channel_input)
        channel_id = channel_info.id
        channel_username = channel_info.username or None
        channel_title = channel_info.title or str(channel_id)

        forcesub_collection.update_one(
            {"chat_id": chat_id},
            {
                "$set": {
                    "channel_id": channel_id,
                    "channel_username": channel_username,
                    "channel_title": channel_title,
                }
            },
            upsert=True,
        )

        link_text = (
            f"[{channel_title}](https://t.me/{channel_username})"
            if channel_username
            else f"`{channel_id}`"
        )
        await message.reply_text(
            f"✅ <b>Force subscription set!</b>\n\n"
            f"📢 Channel: {link_text}\n"
            f"👥 Users who message in this group must be subscribed.\n\n"
            f"<i>Make sure the bot is an admin in that channel with <b>Invite Members</b> permission.</i>",
            disable_web_page_preview=True,
        )

    except Exception as e:
        await message.reply_text(
            f"❌ <b>Failed to set force subscription.</b>\n\n"
            f"<code>{e}</code>\n\n"
            f"<i>Make sure I can access the channel.</i>"
        )


# ─── Core check function ──────────────────────────────────────────────────────
async def check_forcesub(client: Client, message: Message) -> bool:
    """
    Returns True if user is allowed (subscribed or no fsub set).
    Returns False if user is NOT subscribed and must join.
    Sends a join prompt when False.
    """
    chat_id = message.chat.id

    if message.from_user is None:
        return True  # bots / anonymous admins — allow

    user_id = message.from_user.id

    # Ignore admins in the group — they always pass
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return True
    except Exception:
        pass

    # Ignore sudoers
    if user_id in SUDOERS:
        return True

    forcesub_data = forcesub_collection.find_one({"chat_id": chat_id})
    if not forcesub_data:
        return True  # No fsub configured

    channel_id = forcesub_data["channel_id"]
    channel_username = forcesub_data.get("channel_username")
    channel_title = forcesub_data.get("channel_title", "Channel")

    try:
        user_member = await app.get_chat_member(channel_id, user_id)
        # User is banned or left — treat as not subscribed
        if user_member.status in [
            ChatMemberStatus.BANNED,
            ChatMemberStatus.LEFT,
        ]:
            raise UserNotParticipant
        return True  # User is subscribed ✅
    except UserNotParticipant:
        # Build channel URL
        if channel_username:
            channel_url = f"https://t.me/{channel_username}"
        else:
            try:
                channel_url = await app.export_chat_invite_link(channel_id)
            except Exception:
                # Can't get link; silently allow to avoid false blocks
                return True

        try:
            sent = await message.reply_photo(
                photo="https://envs.sh/Tn_.jpg",
                caption=(
                    f"<blockquote>"
                    f"🔒 <b>Channel Subscription Required</b>\n\n"
                    f"👋 Hello {message.from_user.mention}!\n\n"
                    f"To send messages in this group, you must join:\n"
                    f"📢 <b>{channel_title}</b>\n\n"
                    f"After joining, tap <b>I Joined — Check Again</b> below."
                    f"</blockquote>"
                ),
                reply_markup=_fsub_markup(channel_url),
            )
            # Auto-delete the prompt after 60 seconds
            asyncio.create_task(_auto_delete(sent, 60))
        except Exception as e:
            print(f"[ForceSub] Failed to send join prompt: {e}")
        return False  # Not subscribed ❌
    except ChatAdminRequired:
        # Bot is no longer admin in the channel; auto-disable
        forcesub_collection.delete_one({"chat_id": chat_id})
        try:
            await message.reply_text(
                "⚠️ <b>Force subscription disabled.</b>\n"
                "Bot is no longer an admin in the subscribed channel."
            )
        except Exception:
            pass
        return True
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return True
    except Exception as e:
        print(f"[ForceSub] Unexpected error: {e}")
        return True  # On unknown error, allow to avoid false blocks


async def _auto_delete(message, delay: int):
    """Delete a message after `delay` seconds."""
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except Exception:
        pass


# ─── "I Joined" callback ─────────────────────────────────────────────────────
@app.on_callback_query(filters.regex("fsub_check"))
async def fsub_check_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    forcesub_data = forcesub_collection.find_one({"chat_id": chat_id})
    if not forcesub_data:
        await callback_query.answer("✅ Force subscription is no longer active!", show_alert=True)
        try:
            await callback_query.message.delete()
        except Exception:
            pass
        return

    channel_id = forcesub_data["channel_id"]
    channel_username = forcesub_data.get("channel_username")
    channel_title = forcesub_data.get("channel_title", "Channel")

    try:
        user_member = await app.get_chat_member(channel_id, user_id)
        if user_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.LEFT]:
            raise UserNotParticipant
        # Subscribed!
        await callback_query.answer("✅ Verified! You can now send messages.", show_alert=True)
        try:
            await callback_query.message.delete()
        except Exception:
            pass
    except UserNotParticipant:
        channel_url = (
            f"https://t.me/{channel_username}"
            if channel_username
            else await app.export_chat_invite_link(channel_id)
        )
        await callback_query.answer(
            f"❌ You haven't joined {channel_title} yet! Please join and try again.",
            show_alert=True,
        )
    except Exception as e:
        await callback_query.answer(f"Error: {e}", show_alert=True)


@app.on_callback_query(filters.regex("close_force_sub"))
async def close_force_sub(client: Client, callback_query: CallbackQuery):
    await callback_query.answer("Closed!")
    try:
        await callback_query.message.delete()
    except Exception:
        pass


# ─── Enforce fsub on every group message ─────────────────────────────────────
@app.on_message(filters.group & ~filters.service, group=30)
async def enforce_forcesub(client: Client, message: Message):
    allowed = await check_forcesub(client, message)
    if not allowed:
        # Stop the message from being processed by other handlers
        try:
            await message.stop_propagation()
        except Exception:
            pass


__MODULE__ = "ғsᴜʙ"
__HELP__ = """
<b>🔒 Force Subscription</b>

Require users to join a channel before they can send messages in your group.

<b>Commands:</b>
• /fsub @channel — Set force subscription channel
• /fsub -100xxx  — Use numeric channel ID
• /fsub off      — Disable force subscription

<b>Notes:</b>
• Bot must be admin in the channel with <i>Invite Members</i> permission
• Group admins and sudoers are never blocked
• Users get a join prompt with a verification button
"""
