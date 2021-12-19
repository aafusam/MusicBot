#MusicBot <https://t.me/AafuSam_MusciBot>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
👋 Hey There, [{}](tg://user?id={}), **〽️ This Is AafuSam MusicBot To Download YouTube Music. Made With ❤️ By @AafuSam13**
     
Syntax : ```/sam Faded```
      
Maintained By @AafuSam13 🔥
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="❤️Join Our Movies Channel♀️", url="https://t.me/Apkapkapak_Movies"
                    ),
                    InlineKeyboardButton(
                        text="〽️Owner Contact", url="https://t.me/AafuSam13"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("""
AafuSam_MovieBot Successfully Deployed""")
idle()
