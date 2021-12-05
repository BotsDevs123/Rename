#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & PR0FESS0R-99

import os
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION_TEXT = """
<b><u>📣 Join Movies Channel 📣</b></u>

• @Malayalam_Dubbed_MovieZ
• @Night_MovieZ
• @MovieZ_Store

<u><b>🤖 Movies Bot 🤖</b></u>

• @LuciferMoringstar_Robot
• @DonLee_Robot
• @GhostRider_Robot

[⚠️ Share Maximum ⚠️](https://t.me/share/url?url=%E0%B4%A8%E0%B4%AE%E0%B4%B8%E0%B5%8D%E0%B4%95%E0%B4%BE%E0%B4%B0%E0%B4%82%20%E0%B4%8E%E0%B4%B2%E0%B5%8D%E0%B4%B2%E0%B4%BE%E0%B4%B5%E0%B5%BC%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%82%20%E0%B4%B8%E0%B5%81%E0%B4%96%E0%B4%AE%E0%B4%BE%E0%B4%A3%E0%B5%8B%3F%0A%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20Ghost%20Rider%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20TG%20Username%20%40GhostRider_Robot%0A%E0%B4%A8%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%BE%20%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%86%20%20PM%E0%B5%BD%20%E0%B4%B5%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20%E0%B4%A8%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%BE%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%8D%20%E0%B4%86%E0%B4%B5%E0%B4%B6%E0%B5%8D%E0%B4%AF%E0%B4%AE%E0%B5%81%E0%B4%B3%E0%B5%8D%E0%B4%B3%20%E0%B4%AE%E0%B4%B2%E0%B4%AF%E0%B4%BE%E0%B4%B3%E0%B4%82%20%E0%B4%A1%E0%B4%AC%E0%B5%8D%E0%B4%AC%E0%B5%8D%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%A4%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%AF%E0%B5%81%E0%B4%9F%E0%B5%86%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20%E0%B4%9F%E0%B5%88%E0%B4%AA%E0%B5%8D%E0%B4%AA%E0%B5%8D%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%A4%E0%B4%BE%E0%B5%BD%2C%20%E0%B4%9E%E0%B4%BE%E0%B5%BB%20%E0%B4%86%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%20%E0%B4%89%E0%B4%A3%E0%B5%8D%E0%B4%9F%E0%B4%95%E0%B4%BF%E0%B5%BD%20%E0%B4%A4%E0%B5%87%E0%B4%B0%E0%B5%81%E0%B4%82...%21%0A%0A%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20Ghost%20Rider%20Robot)
"""

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"<b>{kopp.file_name}</b>\n\n{CAPTION_TEXT}")

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id
