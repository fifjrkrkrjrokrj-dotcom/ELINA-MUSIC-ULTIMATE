from pyrogram import filters
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from ShrutiMusic import app
from ShrutiMusic.utils.database import get_lang, set_lang
from ShrutiMusic.utils.decorators import ActualAdminCB, language, languageCB
from config import BANNED_USERS
from strings import get_string, languages_present

from config import styled_button

def lanuages_keyboard(_):
    # Build language buttons in rows of 2
    lang_buttons = [
        styled_button(
            text=languages_present[i],
            callback_data=f"languages:{i}",
            style=enums.ButtonStyle.PRIMARY,
        )
        for i in languages_present
    ]
    # Split into rows of 2
    rows = [lang_buttons[i:i+2] for i in range(0, len(lang_buttons), 2)]
    # Add back/close row
    rows.append([
        styled_button(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
            style=enums.ButtonStyle.PRIMARY,
        ),
        styled_button(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=enums.ButtonStyle.DANGER,
        ),
    ])
    return InlineKeyboardMarkup(rows)

@app.on_message(filters.command(["lang", "setlang", "language"]) & ~BANNED_USERS)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["lang_1"],
        reply_markup=keyboard,
    )

@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)

@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(_["lang_4"], show_alert=True)
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(_["lang_2"], show_alert=True)
    except:
        _ = get_string(old)
        return await CallbackQuery.answer(
            _["lang_3"],
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
