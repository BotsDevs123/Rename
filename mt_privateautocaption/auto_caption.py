#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & PR0FESS0R-99

import os
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait


CAP = """[𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗡𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 𝗧𝗢 𝗠𝗬 𝗬𝗢𝗨𝗧𝗨𝗕𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟. 𝗚𝗢 𝗤𝗨𝗜𝗖𝗞𝗟𝗬 𝗔𝗡𝗗 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘](https://youtube.com/c/MoTech_YT)"""


@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"<b>{kopp.file_name}</b>\n\n{CAP}")

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
