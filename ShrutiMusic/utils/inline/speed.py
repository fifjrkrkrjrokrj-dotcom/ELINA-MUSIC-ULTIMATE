# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import styled_button


from pyrogram import enums
def speed_markup(_, chat_id):
    upl = InlineKeyboardMarkup(
        [
            [
                styled_button(
                    text="🕒 0.5x",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                    style=enums.ButtonStyle.PRIMARY,
                ),
                styled_button(
                    text="🕓 0.75x",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                    style=enums.ButtonStyle.PRIMARY,
                ),
            ],
            [
                styled_button(
                    text=_["P_B_4"],
                    callback_data=f"SpeedUP {chat_id}|1.0",
                    style=enums.ButtonStyle.PRIMARY,
                ),
            ],
            [
                styled_button(
                    text="🕤 1.5x",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                    style=enums.ButtonStyle.PRIMARY,
                ),
                styled_button(
                    text="🕛 2.0x",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                    style=enums.ButtonStyle.PRIMARY,
                ),
            ],
            [
                styled_button(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=enums.ButtonStyle.DANGER,
                ),
            ],
        ]
    )
    return upl


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
