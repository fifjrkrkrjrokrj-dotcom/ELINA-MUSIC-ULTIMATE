from datetime import datetime, timedelta
import pytz
import os
import random
import asyncio
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatType, ParseMode
from telegraph import upload_file
from PIL import Image, ImageDraw
import requests

from ShrutiMusic.utils import get_image, get_couple, save_couple
from ShrutiMusic import app

from config import styled_button

def _today():
    return datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%d/%m/%Y")

def _tomorrow():
    return (datetime.now(pytz.timezone("Asia/Kolkata")) + timedelta(days=1)).strftime("%d/%m/%Y")

def make_mention(user_id, name):
    return f'<a href="tg://user?id={user_id}">{name}</a>'

def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
    return path


@app.on_message(filters.command(["couple", "couples"]))
async def ctest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.")

    os.makedirs("downloads", exist_ok=True)
    p1_path = "downloads/pfp.png"
    p2_path = "downloads/pfp1.png"
    test_image_path = f"downloads/test_{cid}.png"
    cppic_path = "downloads/cppic.png"

    today = _today()
    tomorrow = _tomorrow()
    try:
        is_selected = await get_couple(cid, today)
        if not is_selected:
            msg = await message.reply_text("❣️")
            list_of_users = []

            async for i in app.get_chat_members(message.chat.id, limit=50):
                if not i.user.is_bot and not i.user.is_deleted:
                    list_of_users.append(i.user.id)

            if len(list_of_users) < 2:
                await msg.delete()
                return await message.reply_text("Not enough eligible users to pick a couple.")

            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c2_id = random.choice(list_of_users)

            photo1 = (await app.get_chat(c1_id)).photo
            photo2 = (await app.get_chat(c2_id)).photo

            c1_user = await app.get_users(c1_id)
            c2_user = await app.get_users(c2_id)
            N1 = make_mention(c1_id, c1_user.first_name)
            N2 = make_mention(c2_id, c2_user.first_name)

            try:
                p1 = await app.download_media(photo1.big_file_id, file_name=p1_path)
            except Exception:
                p1 = download_image(
                    "https://telegra.ph/file/05aa686cf52fc666184bf.jpg", p1_path
                )
            try:
                p2 = await app.download_media(photo2.big_file_id, file_name=p2_path)
            except Exception:
                p2 = download_image(
                    "https://telegra.ph/file/05aa686cf52fc666184bf.jpg", p2_path
                )

            try:
                img1 = Image.open(p1)
                img2 = Image.open(p2)
            except Exception:
                await msg.delete()
                return await message.reply_text("Could not process profile photos.")

            background_image_path = download_image(
                "https://telegra.ph/file/96f36504f149e5680741a.jpg", cppic_path
            )
            try:
                img = Image.open(background_image_path)
            except Exception:
                await msg.delete()
                return await message.reply_text("Could not load background image.")

            img1 = img1.resize((437, 437))
            img2 = img2.resize((437, 437))

            mask = Image.new("L", img1.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + img1.size, fill=255)

            mask1 = Image.new("L", img2.size, 0)
            draw = ImageDraw.Draw(mask1)
            draw.ellipse((0, 0) + img2.size, fill=255)

            img1.putalpha(mask)
            img2.putalpha(mask1)

            draw = ImageDraw.Draw(img)

            img.paste(img1, (116, 160), img1)
            img.paste(img2, (789, 160), img2)

            img.save(test_image_path)

            TXT = f"""
<b>Tᴏᴅᴀʏ's ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ❤️:

{N1} + {N2} = 💚

Nᴇxᴛ ᴄᴏᴜᴘʟᴇs ᴡɪʟʟ ʙᴇ sᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow}!!</b>
            """

            await message.reply_photo(
                test_image_path,
                caption=TXT,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            styled_button(
                                text="Aᴅᴅ ᴍᴇ 🌋",
                                url=f"https://t.me/{app.username}?startgroup=true",
                                style=enums.ButtonStyle.PRIMARY,
                            )
                        ]
                    ]
                ),
            )

            await msg.delete()
            try:
                a = upload_file(test_image_path)
                for x in a:
                    img_url = "https://graph.org/" + x
                    couple = {"c1_id": c1_id, "c2_id": c2_id}
                    await save_couple(cid, today, couple, img_url)
            except Exception as e:
                print(f"Error saving couple: {e}")

        else:
            msg = await message.reply_text("❣️")
            b = await get_image(cid)
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_user = await app.get_users(c1_id)
            c2_user = await app.get_users(c2_id)
            c1_name = c1_user.first_name
            c2_name = c2_user.first_name

            TXT = f"""
<b>Tᴏᴅᴀʏ's ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ 🎉:

{make_mention(c1_id, c1_name)} + {make_mention(c2_id, c2_name)} = ❣️

Nᴇxᴛ ᴄᴏᴜᴘʟᴇs ᴡɪʟʟ ʙᴇ sᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow}!!</b>
            """
            await message.reply_photo(
                b,
                caption=TXT,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            styled_button(
                                text="Aᴅᴅ ᴍᴇ🌋",
                                url=f"https://t.me/{app.username}?startgroup=true",
                                style=enums.ButtonStyle.PRIMARY,
                            )
                        ]
                    ]
                ),
            )
            await msg.delete()

    except Exception as e:
        print(f"couple error: {e}")
        try:
            await message.reply_text("Something went wrong. Please try again later.")
        except Exception:
            pass
    finally:
        try:
            os.remove(p1_path)
            os.remove(p2_path)
            os.remove(test_image_path)
            os.remove(cppic_path)
        except Exception as cleanup_error:
            print(f"Error during cleanup: {cleanup_error}")
