import random
from typing import Union

from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ShrutiMusic import app
from config import styled_button

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]

# ── Custom Premium Emoji IDs from user's list ──────────────────────────
_ICON_CROWN       = 5276507128616475659  # 🫅
_ICON_MEGAPHONE   = 5424818078833715060  # 📣
_ICON_NEUTRAL     = 5438274168422409988  # 😐
_ICON_BLOCKED     = 5260293700088511294  # ⛔️
_ICON_SUN         = 5402477260982731644  # ☀️
_ICON_EXPLOSION   = 5276032951342088188  # 💥
_ICON_MOON        = 5449569374065152798  # 🌛
_ICON_GEAR        = 5341715473882955310  # ⚙️
_ICON_ROCKET      = 5195033767969839232  # 🚀
_ICON_PLAY        = 5264919878082509254  # ▶️
_ICON_SHUFFLE     = 5409109841538994759  # 🌈
_ICON_SEEK        = 5399913388845322366  # 🌧
_ICON_DOWNLOAD    = 6114041466621792865  # 🎁
_ICON_SPEED       = 5388632425314140043  # 🔈
_ICON_PRIVACY     = 5940757394702211878  # 🤍
_ICON_GAMES       = 6073153120265835101  # 🥳
_ICON_WARN        = 6073345844038341830  # ➡️
_ICON_TELEGRAPH   = 5197576684961808524  # 🎆
_ICON_TAG         = 5197326034965379636  # 🚩
_ICON_TTS         = 5388632425314140043  # 🔈
_ICON_INVITE      = 5208902681225083086  # 🥂
_ICON_FSUB        = 5296369303661067030  # 🔒
_ICON_ZOMBIE      = 5438274168422409988  # 😐
_ICON_INFO        = 5282843764451195532  # 🖥
_ICON_GITHUB      = 5440621591387980068  # Github Star
_ICON_TD          = 6230870289379495036  # ☺️
_ICON_MONGO       = 5256106411917592822  # 💡
_ICON_FONT        = 6231204704123096753  # 💕
_ICON_BOTS        = 6071239497587102212  # 😎
_ICON_WISH        = 6051088683560344657  # 🌟
_ICON_WELCOME     = 6231271181626903902  # 🎀
_ICON_COUPLE      = 6231204704123096753  # 💕
_ICON_LOVEBIRDS   = 5276185255177372874  # 🌹
_ICON_VCLOGGER    = 5424818078833715060  # 📣
_ICON_BACK        = 6084861780935315826  # 🔙
_ICON_LANGUAGE    = 5447410659077661506  # 🌐

def _rand_two():
    a = random.choice(STYLES)
    b = random.choice([s for s in STYLES if s != a])
    return a, b

def help_pannel_page1(_, START: Union[bool, int] = None):
    alone_style, group_style = _rand_two()
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_1"], callback_data="help_callback hb1", style=group_style, icon_custom_emoji_id=_ICON_GEAR),
                styled_button(text=_["H_B_2"], callback_data="help_callback hb2", style=group_style, icon_custom_emoji_id=_ICON_CROWN),
            ],
            [
                styled_button(text=_["H_B_3"], callback_data="help_callback hb3", style=group_style, icon_custom_emoji_id=_ICON_MEGAPHONE),
                styled_button(text=_["H_B_4"], callback_data="help_callback hb4", style=group_style, icon_custom_emoji_id=_ICON_BLOCKED),
            ],
            [
                styled_button(text=_["H_B_5"], callback_data="help_callback hb5", style=group_style, icon_custom_emoji_id=_ICON_BLOCKED),
                styled_button(text=_["H_B_6"], callback_data="help_callback hb6", style=group_style, icon_custom_emoji_id=_ICON_PLAY),
                styled_button(text=_["H_B_7"], callback_data="help_callback hb7", style=group_style, icon_custom_emoji_id=_ICON_EXPLOSION),
            ],
            [
                styled_button(text=_["H_B_8"], callback_data="help_callback hb8", style=group_style, icon_custom_emoji_id=_ICON_MOON),
                styled_button(text=_["H_B_9"], callback_data="help_callback hb9", style=group_style, icon_custom_emoji_id=_ICON_GEAR),
                styled_button(text=_["H_B_10"], callback_data="help_callback hb10", style=group_style, icon_custom_emoji_id=_ICON_ROCKET),
            ],
            [
                styled_button(text=_["S_B_12"], callback_data="LG", style=alone_style, icon_custom_emoji_id=_ICON_LANGUAGE)
            ],
            [
                styled_button(text="⏮", callback_data="help_page_4", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=alone_style if START else enums.ButtonStyle.DANGER,
                    icon_custom_emoji_id=_ICON_BACK
                ),
                styled_button(text="⏭", callback_data="help_page_2", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
            ],
        ]
    )

def help_pannel_page2(_, START: Union[bool, int] = None):
    alone_style, group_style = _rand_two()
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_11"], callback_data="help_callback hb11", style=group_style, icon_custom_emoji_id=_ICON_PLAY),
                styled_button(text=_["H_B_12"], callback_data="help_callback hb12", style=group_style, icon_custom_emoji_id=_ICON_SHUFFLE),
            ],
            [
                styled_button(text=_["H_B_13"], callback_data="help_callback hb13", style=group_style, icon_custom_emoji_id=_ICON_SEEK),
                styled_button(text=_["H_B_14"], callback_data="help_callback hb14", style=group_style, icon_custom_emoji_id=_ICON_DOWNLOAD),
            ],
            [
                styled_button(text=_["H_B_15"], callback_data="help_callback hb15", style=group_style, icon_custom_emoji_id=_ICON_SPEED),
                styled_button(text=_["H_B_16"], callback_data="help_callback hb16", style=group_style, icon_custom_emoji_id=_ICON_PRIVACY),
                styled_button(text=_["H_B_17"], callback_data="help_callback hb17", style=group_style, icon_custom_emoji_id=_ICON_GAMES),
            ],
            [
                styled_button(text=_["H_B_18"], callback_data="help_callback hb18", style=group_style, icon_custom_emoji_id=_ICON_WARN),
                styled_button(text=_["H_B_19"], callback_data="help_callback hb19", style=group_style, icon_custom_emoji_id=_ICON_TELEGRAPH),
                styled_button(text=_["H_B_20"], callback_data="help_callback hb20", style=group_style, icon_custom_emoji_id=_ICON_TAG),
            ],
            [
                styled_button(text=_["S_B_12"], callback_data="LG", style=alone_style, icon_custom_emoji_id=_ICON_LANGUAGE)
            ],
            [
                styled_button(text="⏮", callback_data="help_page_1", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=alone_style if START else enums.ButtonStyle.DANGER,
                    icon_custom_emoji_id=_ICON_BACK
                ),
                styled_button(text="⏭", callback_data="help_page_3", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
            ],
        ]
    )

def help_pannel_page3(_, START: Union[bool, int] = None):
    alone_style, group_style = _rand_two()
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_21"], callback_data="help_callback hb21", style=group_style, icon_custom_emoji_id=_ICON_DOWNLOAD),
                styled_button(text=_["H_B_22"], callback_data="help_callback hb22", style=group_style, icon_custom_emoji_id=_ICON_TTS),
            ],
            [
                styled_button(text=_["H_B_23"], callback_data="help_callback hb23", style=group_style, icon_custom_emoji_id=_ICON_INVITE),
                styled_button(text=_["H_B_24"], callback_data="help_callback hb24", style=group_style, icon_custom_emoji_id=_ICON_FSUB),
            ],
            [
                styled_button(text=_["H_B_25"], callback_data="help_callback hb25", style=group_style, icon_custom_emoji_id=_ICON_ZOMBIE),
                styled_button(text=_["H_B_26"], callback_data="help_callback hb26", style=group_style, icon_custom_emoji_id=_ICON_INFO),
                styled_button(text=_["H_B_27"], callback_data="help_callback hb27", style=group_style, icon_custom_emoji_id=_ICON_GITHUB),
            ],
            [
                styled_button(text=_["H_B_28"], callback_data="help_callback hb28", style=group_style, icon_custom_emoji_id=_ICON_TD),
                styled_button(text=_["H_B_29"], callback_data="help_callback hb29", style=group_style, icon_custom_emoji_id=_ICON_MONGO),
                styled_button(text=_["H_B_30"], callback_data="help_callback hb30", style=group_style, icon_custom_emoji_id=_ICON_FONT),
            ],
            [
                styled_button(text=_["S_B_12"], callback_data="LG", style=alone_style, icon_custom_emoji_id=_ICON_LANGUAGE)
            ],
            [
                styled_button(text="⏮", callback_data="help_page_2", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=alone_style if START else enums.ButtonStyle.DANGER,
                    icon_custom_emoji_id=_ICON_BACK
                ),
                styled_button(text="⏭", callback_data="help_page_4", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
            ],
        ]
    )

def help_pannel_page4(_, START: Union[bool, int] = None):
    alone_style, group_style = _rand_two()
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_31"], callback_data="help_callback hb31", style=group_style, icon_custom_emoji_id=_ICON_NEUTRAL),
                styled_button(text=_["H_B_32"], callback_data="help_callback hb32", style=group_style, icon_custom_emoji_id=_ICON_BOTS),
            ],
            [
                styled_button(text=_["H_B_33"], callback_data="help_callback hb33", style=group_style, icon_custom_emoji_id=_ICON_INFO),
                styled_button(text=_["H_B_34"], callback_data="help_callback hb34", style=group_style, icon_custom_emoji_id=_ICON_WISH),
            ],
            [
                styled_button(text=_["H_B_35"], callback_data="help_callback hb35", style=group_style, icon_custom_emoji_id=_ICON_WELCOME),
                styled_button(text=_["H_B_37"], callback_data="help_callback hb37", style=group_style, icon_custom_emoji_id=_ICON_COUPLE),
            ],
            [
                styled_button(text=_["H_B_38"], callback_data="help_callback hb38", style=group_style, icon_custom_emoji_id=_ICON_LOVEBIRDS),
                styled_button(text=_["H_B_39"], callback_data="help_callback hb39", style=group_style, icon_custom_emoji_id=_ICON_VCLOGGER),
            ],
            [
                styled_button(text=_["H_B_36"], callback_data="help_callback hb36", style=group_style, icon_custom_emoji_id=_ICON_PLAY),
            ],   
            [
                styled_button(text=_["S_B_12"], callback_data="LG", style=alone_style, icon_custom_emoji_id=_ICON_LANGUAGE)
            ],
            [
                styled_button(text="⏮", callback_data="help_page_3", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=alone_style if START else enums.ButtonStyle.DANGER,
                    icon_custom_emoji_id=_ICON_BACK
                ),
                styled_button(text="⏭", callback_data="help_page_1", style=alone_style, icon_custom_emoji_id=_ICON_BACK),
            ],
        ]
    )

def help_back_markup(_, page: int = 1):
    alone_style = random.choice(STYLES)
    return InlineKeyboardMarkup(
        [
            [
                styled_button(
                    text=_["BACK_BUTTON"],
                    callback_data=f"help_page_{page}",
                    style=alone_style,
                    icon_custom_emoji_id=_ICON_BACK
                )
            ]
        ]
    )


def private_help_panel(_):
    alone_style = random.choice(STYLES)
    return [
        [
            styled_button(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                style=alone_style,
                icon_custom_emoji_id=_ICON_GEAR
            ),
        ]
    ]
