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
def stats_buttons(_, status):
    not_sudo = [
        styled_button(
            text=_["SA_B_1"],
            callback_data="TopOverall",
            style=enums.ButtonStyle.PRIMARY,
        )
    ]
    sudo = [
        styled_button(
            text=_["SA_B_2"],
            callback_data="bot_stats_sudo",
            style=enums.ButtonStyle.PRIMARY,
        ),
        styled_button(
            text=_["SA_B_3"],
            callback_data="TopOverall",
            style=enums.ButtonStyle.PRIMARY,
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
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


def back_stats_buttons(_):
    upl = InlineKeyboardMarkup(
        [
            [
                styled_button(
                    text=_["BACK_BUTTON"],
                    callback_data="stats_back",
                    style=enums.ButtonStyle.PRIMARY,
                ),
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
