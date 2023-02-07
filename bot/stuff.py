#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .config import CREATOR
from .worker import *


async def up(event):
    # if not event.is_private:
    # return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌤 Pɪɴɢ = `{ms}ms` 🌥"
    await event.reply(f"🚦 Uᴘᴛɪᴍᴇ : {v} 🚦 \n\n" + p)


async def start(event):
    try:
        await event.reply(
            f"𝐇𝐞𝐲 [{event.sender.first_name}](tg://user?id={event.sender_id}) \n\n☛ 𝐈 𝐚𝐦 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐄𝐧𝐜𝐨𝐝𝐞𝐫 𝐁𝐨𝐭 𝐟𝐫𝐨𝐦 𝐕𝐢𝐝𝐞𝐨𝐬 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐟𝐫𝐨𝐦 𝐓𝐆 𝐨𝐫 𝐟𝐫𝐨𝐦 𝐃𝐢𝐫𝐞𝐜𝐭 𝐀𝐜𝐜𝐞𝐬𝐬 !! \n\n 𝐈 𝐚𝐦 𝐑𝐞𝐚𝐝𝐢𝐥𝐲 𝐑𝐞𝐝𝐮𝐜𝐞 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 𝐮𝐬𝐢𝐧𝐠 𝐣𝐮𝐬𝐭 𝐅𝐅𝐌𝐏𝐄𝐆 𝐚𝐬 𝐬𝐮𝐠𝐠𝐞𝐬𝐭𝐞𝐝 𝐛𝐲 𝐦𝐚𝐬𝐭𝐞𝐫 !!. \n\n ♨️MAINTAINED BY♨️ : [Click Here](tg://user?id={CREATOR}) ",
            buttons=[
                [Button.inline("📮 HELP 📮", data="ihelp")],
                [
                    Button.url("⚡ CHANNEL ⚡", url="t.me/FuZionX"),
                    Button.url("🧑‍💻 DEV 🧑‍💻", url="t.me/NoHelloMe"),
                ],
            ],
        )
    except Exception as e:
        LOGS.info(e)


async def beck(event):
    try:
        # if ev.data == "beck":
        # await ev.answer()
        await event.edit(
            f"𝐇𝐞𝐲 [{event.sender.first_name}](tg://user?id={event.sender_id}) \n\n☛ 𝐈 𝐚𝐦 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐄𝐧𝐜𝐨𝐝𝐞𝐫 𝐁𝐨𝐭 𝐟𝐫𝐨𝐦 𝐕𝐢𝐝𝐞𝐨𝐬 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐟𝐫𝐨𝐦 𝐓𝐆 𝐨𝐫 𝐟𝐫𝐨𝐦 𝐃𝐢𝐫𝐞𝐜𝐭 𝐀𝐜𝐜𝐞𝐬𝐬 !! \n\n 𝐈 𝐚𝐦 𝐑𝐞𝐚𝐝𝐢𝐥𝐲 𝐑𝐞𝐝𝐮𝐜𝐞 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 𝐮𝐬𝐢𝐧𝐠 𝐣𝐮𝐬𝐭 𝐅𝐅𝐌𝐏𝐄𝐆 𝐚𝐬 𝐬𝐮𝐠𝐠𝐞𝐬𝐭𝐞𝐝 𝐛𝐲 𝐦𝐚𝐬𝐭𝐞𝐫 !!. \n\n ♨️MAINTAINED BY♨️ : [Click Here](tg://user?id={CREATOR}) ",
            buttons=[
                [Button.inline("📮 HELP 📮", data="ihelp")],
                [
                    Button.url("⚡ CHANNEL ⚡", url="t.me/FuZionX"),
                    Button.url("🧑‍💻 DEV 🧑‍💻", url="t.me/NoHelloMe"),
                ],
            ],
        )
    except Exception as ek:
        LOGS.info(ek)


async def ihelp(e):
    try:
        hp = """📑 `I am Insane Encoder Bot !!` 📑

⚙ `FEATURES` ⚙ ::

📌 Encode Big Files by /dl via DDL to Bypass Telegram Limit
📌 Send Telegram Files to Encode by /encode
📌 I can Do Anything As you need for your encode
📌 You can Customize the `FFMPEG` anytime via /setffmpeg Command
📌 I am Filled with libfdk_aac Library of FFMPEG which is Best to Give HE-AAC Audio Quality !!
"""
        await e.edit(
            hp,
            buttons=[
                [Button.inline("Back ↩", data="beck")],
            ],
        )
    except Exception as h:
        LOGS.info(h)


async def help(e):
    # For /help Command
    try:
        hp = """📑 `I am Insane Encoder Bot !!` 📑

⚙ `FEATURES` ⚙ ::

📌 Encode Big Files by /dl via DDL to Bypass Telegram Limit
📌 Send Telegram Files to Encode by /encode
📌 I can Do Anything As you need for your encode
📌 You can Customize the `FFMPEG` anytime via /setffmpeg Command
📌 I am Filled with libfdk_aac Library of FFMPEG which is Best to Give HE-AAC Audio Quality !!
"""
        await e.reply(
            hp,
            buttons=[
                [Button.inline("Back ↩", data="beck")],
            ],
        )
    except Exception as h:
        LOGS.info(h)
