"""
Button bridge module using python-telegram-bot v22.7 style serialization.

python-telegram-bot natively supports style="primary"/"success"/"danger"
on InlineKeyboardButton, providing the correct serialization for Telegram
colored inline buttons as defined in Bot API 6.7+.

This module re-exports what is defined in config.py. For direct use,
import from config:

    from config import styled_button, style_primary, style_success, style_danger

Or use the string constants directly:

    btn = styled_button("Play", callback_data="play", style="success")
"""

import config

styled_button = config.styled_button
STYLE_PRIMARY = config.STYLE_PRIMARY
STYLE_SUCCESS = config.STYLE_SUCCESS
STYLE_DANGER = config.STYLE_DANGER
STYLE_CHOICES = config.STYLE_CHOICES
alone = config.alone_style
group = config.group_style
