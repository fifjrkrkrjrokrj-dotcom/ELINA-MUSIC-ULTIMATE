import asyncio
import importlib
import ssl

try:
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass

# Bypassing SSL globally for HTTPX (used by py_yt/youtube-search-python)
import httpx
_orig_async_init = httpx.AsyncClient.__init__
def _patched_async_init(self, *args, **kwargs):
    kwargs["verify"] = False
    _orig_async_init(self, *args, **kwargs)
httpx.AsyncClient.__init__ = _patched_async_init

_orig_sync_init = httpx.Client.__init__
def _patched_sync_init(self, *args, **kwargs):
    kwargs["verify"] = False
    _orig_sync_init(self, *args, **kwargs)
httpx.Client.__init__ = _patched_sync_init

import pyrogram.raw.types
from pyrogram.raw.types import PeerChat, PeerChannel, PeerUser


def _group_call_chat_id(self):
    peer = getattr(self, "peer", None)
    if peer:
        if isinstance(peer, PeerChannel):
            return peer.channel_id
        elif isinstance(peer, PeerChat):
            return peer.chat_id
        elif isinstance(peer, PeerUser):
            return peer.user_id
    return 0

# Monkeypatch UpdateGroupCall to expose chat_id property dynamically
pyrogram.raw.types.UpdateGroupCall.chat_id = property(_group_call_chat_id)



from pyrogram import idle
from pyrogram.types import BotCommand
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS

from ShrutiMusic import LOGGER, app, userbot
from ShrutiMusic.core.call import Nand
from ShrutiMusic.misc import sudo
from ShrutiMusic.plugins import ALL_MODULES
from ShrutiMusic.utils.database import (
    get_banned_users,
    get_gbanned,
)

COMMANDS = [
    BotCommand("start", "❖ sᴛᴀʀᴛ ʙᴏᴛ • ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
    BotCommand("help", "❖ ʜᴇʟᴘ ᴍᴇɴᴜ • ɢᴇᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs"),
    BotCommand("ping", "❖ ᴘɪɴɢ ʙᴏᴛ • ᴄʜᴇᴄᴋ ᴘɪɴɢ"),
    BotCommand("play", "❖ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ɪɴ ᴠᴄ"),
    BotCommand("vplay", "❖ ᴘʟᴀʏ ᴠɪᴅᴇᴏ ɪɴ ᴠᴄ"),
    BotCommand("pause", "❖ ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ"),
    BotCommand("resume", "❖ ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ"),
    BotCommand("skip", "❖ sᴋɪᴘ ᴛʀᴀᴄᴋ"),
    BotCommand("stop", "❖ sᴛᴏᴘ sᴛʀᴇᴀᴍ"),
    BotCommand("queue", "❖ sʜᴏᴡ ᴏ̨ᴜᴇᴜᴇ"),
    BotCommand("song", "❖ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ"),
    BotCommand("tagall", "❖ ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs"),
]


async def setup_bot_commands():
    try:
        await app.set_bot_commands(COMMANDS)
        LOGGER("ShrutiMusic").info(
            "Bot commands set successfully!"
        )

    except Exception as e:
        LOGGER("ShrutiMusic").error(
            f"Failed to set bot commands: {e}"
        )


async def init():

    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "Assistant client variables not defined."
        )
        return

    await sudo()

    try:
        users = await get_gbanned()

        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()

        for user_id in users:
            BANNED_USERS.add(user_id)

    except Exception as e:
        LOGGER("ShrutiMusic").error(
            f"Banned user load error: {e}"
        )

    await app.start()

    LOGGER("ShrutiMusic").info(
        "Bot Started Successfully!"
    )

    await setup_bot_commands()

    # Import Plugins Fix
    for all_module in ALL_MODULES:

        try:
            all_module = (
                all_module
                .replace("\\", ".")
                .replace("/", ".")
            )

            if not all_module.startswith("."):
                all_module = "." + all_module

            importlib.import_module(
                "ShrutiMusic.plugins" + all_module
            )

            LOGGER("ShrutiMusic.plugins").info(
                f"Imported => {all_module}"
            )

        except Exception as e:

            LOGGER("ShrutiMusic.plugins").error(
                f"Failed To Import {all_module} : {e}"
            )

    LOGGER("ShrutiMusic.plugins").info(
        "All Modules Imported!"
    )

    await userbot.start()

    LOGGER("ShrutiMusic").info(
        "Assistant Started!"
    )

    await Nand.start()

    LOGGER("ShrutiMusic").info(
        "Voice Client Started!"
    )

    try:
        await Nand.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )

    except NoActiveGroupCall:

        LOGGER("ShrutiMusic").error(
            "Turn on VC in LOG_GROUP_ID"
        )

    except Exception as e:

        LOGGER("ShrutiMusic").error(
            f"VC Error : {e}"
        )

    try:
        await Nand.decorators()

    except Exception as e:

        LOGGER("ShrutiMusic").error(
            f"Decorator Error : {e}"
        )

    LOGGER("ShrutiMusic").info(
        "Shruti Music Started Successfully!"
    )

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("ShrutiMusic").info(
        "Stopping Shruti Music Bot..."
    )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())