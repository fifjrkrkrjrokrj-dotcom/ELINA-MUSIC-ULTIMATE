import random
from pyrogram import enums
import config
from ShrutiMusic import app
from config import styled_button

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]

# ── New premium emoji IDs from user's collection ───────────────────────────
_ICON_ADD_GROUP   = 6231271181626903902  # 🎀 ribbon
_ICON_SUPPORT     = 6230817173518945714  # 🌸 flower
_ICON_SOURCE      = 5440621591387980068  # GitHub star
_ICON_ABOUT       = 6051088683560344657  # 🌟 star
_ICON_HELP        = 5341715473882955310  # ⚙️ gear
_ICON_OWNER       = 5276507128616475659  # 🫅 crown
_ICON_LANGUAGE    = 5447410659077661506  # 🌐 globe
_ICON_BACK        = 6084861780935315826  # back arrow
_ICON_CHANNEL     = 5377754411319698237  # channel
_ICON_DONATE      = 5395828157687291935  # 🎁 gift
_ICON_YOUTUBE     = 5463107823946717464  # yt
_ICON_GITHUB      = 5440621591387980068  # github
_ICON_PLAY        = 5217933090483098080  # 🎵 music note
_ICON_STAR        = 6231166745202133672  # ⭐️ star variant


def _rand_two():
    """Pick two distinct random styles."""
    a = random.choice(STYLES)
    b = random.choice([s for s in STYLES if s != a])
    return a, b


def start_panel(_):
    alone_style, group_style = _rand_two()
    buttons = [
        [
            styled_button(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=group_style,
                icon_custom_emoji_id=_ICON_ADD_GROUP,
            ),
            styled_button(
                text=_["S_B_2"],
                url=config.SUPPORT_GROUP,
                style=group_style,
                icon_custom_emoji_id=_ICON_SUPPORT,
            ),
        ],
        [
            styled_button(
                text=_["E_X_1"],
                url=config.UPSTREAM_REPO,
                style=group_style,
                icon_custom_emoji_id=_ICON_SOURCE,
            ),
            styled_button(
                text=_["S_B_11"],
                callback_data="about_page",
                style=group_style,
                icon_custom_emoji_id=_ICON_ABOUT,
            ),
        ],
    ]
    return buttons


def private_panel(_):
    alone_style, group_style = _rand_two()
    # Direct link to owner Telegram profile
    owner_url = f"https://t.me/{config.OWNER_USERNAME}" if config.OWNER_USERNAME else f"tg://openmessage?user_id={config.OWNER_ID}"
    buttons = [
        [
            styled_button(
                text=_["S_B_3"],  # Add me to group
                url=f"https://t.me/{app.username}?startgroup=true",
                style=alone_style,
                icon_custom_emoji_id=_ICON_ADD_GROUP,
            ),
        ],
        [
            styled_button(
                text=_["S_B_4"],  # Help and Commands
                callback_data="help_page_1",
                style=alone_style,
                icon_custom_emoji_id=_ICON_HELP,
            ),
        ],
        [
            styled_button(
                text=_["S_B_5"],  # Owner (Links directly to profile now)
                url=owner_url,
                style=group_style,
                icon_custom_emoji_id=_ICON_OWNER,
            ),
            styled_button(
                text=_["S_B_12"],  # Language
                callback_data="LG",
                style=group_style,
                icon_custom_emoji_id=_ICON_LANGUAGE,
            )
        ],
        [
            styled_button(
                text=_["E_X_1"],  # Source
                callback_data="fork_repo",
                style=group_style,
                icon_custom_emoji_id=_ICON_SOURCE,
            ),
            styled_button(
                text=_["S_B_6"],  # About / Updates
                callback_data="about_page",
                style=group_style,
                icon_custom_emoji_id=_ICON_STAR,
            ),
        ],
    ]
    return buttons


def about_panel(_):
    alone_style, group_style = _rand_two()
    buttons = [
        [
            styled_button(
                text=_["S_B_6"],
                url=config.SUPPORT_CHANNEL,
                style=group_style,
                icon_custom_emoji_id=_ICON_CHANNEL,
            ),
            styled_button(
                text=_["S_B_2"],
                url=config.SUPPORT_GROUP,
                style=group_style,
                icon_custom_emoji_id=_ICON_SUPPORT,
            ),
        ],
        [
            styled_button(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
                style=alone_style,
                icon_custom_emoji_id=_ICON_BACK,
            ),
        ],
    ]
    return buttons


def owner_panel(_):
    # Fallback owner panel (normally unused because button links directly)
    alone_style, group_style = _rand_two()
    owner_url = f"https://t.me/{config.OWNER_USERNAME}" if config.OWNER_USERNAME else f"tg://openmessage?user_id={config.OWNER_ID}"
    buttons = [
        [
            styled_button(
                text=_["S_B_5"],
                url=owner_url,
                style=group_style,
                icon_custom_emoji_id=_ICON_OWNER,
            )
        ],
        [
            styled_button(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
                style=alone_style,
                icon_custom_emoji_id=_ICON_BACK,
            )
        ]
    ]
    return buttons
