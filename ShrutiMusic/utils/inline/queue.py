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


from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import styled_button


from pyrogram import enums
def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            styled_button(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=enums.ButtonStyle.DANGER,
            ),
        ]
    ]
    dur = [
        [
            styled_button(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
                style=enums.ButtonStyle.PRIMARY,
            )
        ],
        [
            styled_button(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=enums.ButtonStyle.DANGER,
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                styled_button(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                    style=enums.ButtonStyle.PRIMARY,
                ),
                styled_button(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=enums.ButtonStyle.DANGER,
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            styled_button(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                style=enums.ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
