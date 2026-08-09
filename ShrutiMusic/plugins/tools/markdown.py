from pyrogram import enums
from pyrogram.enums import ChatType, ParseMode
from pyrogram.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from ShrutiMusic import app
from ShrutiMusic.utils.functions import MARKDOWN

from config import styled_button

@app.on_message(command("markdownhelp"))
async def mkdwnhelp(_, m: Message):
    keyb = InlineKeyboardMarkup(
        [
            [
                styled_button(
                    text="Click Here!",
                    url=f"http://t.me/{app.username}?start=mkdwn_help",
                    style=enums.ButtonStyle.PRIMARY,
                )
            ]
        ]
    )
    if m.chat.type != ChatType.PRIVATE:
        await m.reply(
            "ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍᴀʀᴋᴅᴏᴡɴ ᴜsᴀɢᴇ sʏɴᴛᴀx ɪɴ ᴘᴍ!",
            reply_markup=keyb,
        )
    else:
        await m.reply(
            MARKDOWN, parse_mode=ParseMode.HTML, disable_web_page_preview=True
        )
    return
