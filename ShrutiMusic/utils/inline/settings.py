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

from pyrogram.types import InlineKeyboardButton

from config import styled_button


from pyrogram import enums
def setting_markup(_):
    buttons = [
        [
            styled_button(text=_["ST_B_1"], callback_data="AU", style=enums.ButtonStyle.PRIMARY),
            styled_button(text=_["ST_B_3"], callback_data="LG", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(text=_["ST_B_2"], callback_data="PM", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(text=_["ST_B_4"], callback_data="VM", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close", style=enums.ButtonStyle.DANGER),
        ],
    ]
    return buttons


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            styled_button(text="Vᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜", callback_data="VOTEANSWER", style=enums.ButtonStyle.SUCCESS),
            styled_button(
                text=_["ST_B_5"] if mode == True else _["ST_B_6"],
                callback_data="VOMODECHANGE",
                style=enums.ButtonStyle.PRIMARY,
            ),
        ],
        [
            styled_button(text="-2", callback_data="FERRARIUDTI M", style=enums.ButtonStyle.PRIMARY),
            styled_button(
                text=f"ᴄᴜʀʀᴇɴᴛ : {current}",
                callback_data="ANSWERVOMODE",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(text="+2", callback_data="FERRARIUDTI A", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close", style=enums.ButtonStyle.DANGER),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            styled_button(text=_["ST_B_7"], callback_data="AUTHANSWER", style=enums.ButtonStyle.PRIMARY),
            styled_button(
                text=_["ST_B_8"] if status == True else _["ST_B_9"],
                callback_data="AUTH",
                style=enums.ButtonStyle.PRIMARY,
            ),
        ],
        [
            styled_button(text=_["ST_B_1"], callback_data="AUTHLIST", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close", style=enums.ButtonStyle.DANGER),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            styled_button(text=_["ST_B_10"], callback_data="SEARCHANSWER", style=enums.ButtonStyle.PRIMARY),
            styled_button(
                text=_["ST_B_11"] if Direct == True else _["ST_B_12"],
                callback_data="MODECHANGE",
                style=enums.ButtonStyle.PRIMARY,
            ),
        ],
        [
            styled_button(text=_["ST_B_13"], callback_data="AUTHANSWER", style=enums.ButtonStyle.PRIMARY),
            styled_button(
                text=_["ST_B_8"] if Group == True else _["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
                style=enums.ButtonStyle.PRIMARY,
            ),
        ],
        [
            styled_button(text=_["ST_B_14"], callback_data="PLAYTYPEANSWER", style=enums.ButtonStyle.SUCCESS),
            styled_button(
                text=_["ST_B_8"] if Playtype == True else _["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
                style=enums.ButtonStyle.SUCCESS,
            ),
        ],
        [
            styled_button(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close", style=enums.ButtonStyle.DANGER),
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
