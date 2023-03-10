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
    p = f"ð¤ PÉªÉ´É¢ = `{ms}ms` ð¥"
    await event.reply(f"ð¦ Uá´á´Éªá´á´ : {v} ð¦ \n\n" + p)


async def start(event):
    try:
        await event.reply(
            f"ððð² [{event.sender.first_name}](tg://user?id={event.sender_id}) \n\nâ ð ðð¦ ðð¨ð°ðð«ðð®ð¥ ðð§ðð¨ððð« ðð¨ð­ ðð«ð¨ð¦ ðð¢ððð¨ð¬ ðð¨ð°ð§ð¥ð¨ðððð ðð«ð¨ð¦ ðð ð¨ð« ðð«ð¨ð¦ ðð¢ð«ððð­ ððððð¬ð¬ !! \n\n ð ðð¦ ððððð¢ð¥ð² ðððð®ðð ðð¢ð¥ð ðð¢ð³ð ð®ð¬ð¢ð§ð  ð£ð®ð¬ð­ ðððððð ðð¬ ð¬ð®ð ð ðð¬ð­ðð ðð² ð¦ðð¬ð­ðð« !!. \n\n â¨ï¸MAINTAINED BYâ¨ï¸ : [Click Here](tg://user?id={CREATOR}) ",
            buttons=[
                [Button.inline("ð® HELP ð®", data="ihelp")],
                [
                    Button.url("â¡ CHANNEL â¡", url="t.me/FuZionX"),
                    Button.url("ð§âð» DEV ð§âð»", url="t.me/NoHelloMe"),
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
            f"ððð² [{event.sender.first_name}](tg://user?id={event.sender_id}) \n\nâ ð ðð¦ ðð¨ð°ðð«ðð®ð¥ ðð§ðð¨ððð« ðð¨ð­ ðð«ð¨ð¦ ðð¢ððð¨ð¬ ðð¨ð°ð§ð¥ð¨ðððð ðð«ð¨ð¦ ðð ð¨ð« ðð«ð¨ð¦ ðð¢ð«ððð­ ððððð¬ð¬ !! \n\n ð ðð¦ ððððð¢ð¥ð² ðððð®ðð ðð¢ð¥ð ðð¢ð³ð ð®ð¬ð¢ð§ð  ð£ð®ð¬ð­ ðððððð ðð¬ ð¬ð®ð ð ðð¬ð­ðð ðð² ð¦ðð¬ð­ðð« !!. \n\n â¨ï¸MAINTAINED BYâ¨ï¸ : [Click Here](tg://user?id={CREATOR}) ",
            buttons=[
                [Button.inline("ð® HELP ð®", data="ihelp")],
                [
                    Button.url("â¡ CHANNEL â¡", url="t.me/FuZionX"),
                    Button.url("ð§âð» DEV ð§âð»", url="t.me/NoHelloMe"),
                ],
            ],
        )
    except Exception as ek:
        LOGS.info(ek)


async def ihelp(e):
    try:
        hp = """ð `I am Insane Encoder Bot !!` ð

â `FEATURES` â ::

ð Encode Big Files by /dl via DDL to Bypass Telegram Limit
ð Send Telegram Files to Encode by /encode
ð I can Do Anything As you need for your encode
ð You can Customize the `FFMPEG` anytime via /setffmpeg Command
ð I am Filled with libfdk_aac Library of FFMPEG which is Best to Give HE-AAC Audio Quality !!
"""
        await e.edit(
            hp,
            buttons=[
                [Button.inline("Back â©", data="beck")],
            ],
        )
    except Exception as h:
        LOGS.info(h)


async def help(e):
    # For /help Command
    try:
        hp = """ð `I am Insane Encoder Bot !!` ð

â `FEATURES` â ::

ð Encode Big Files by /dl via DDL to Bypass Telegram Limit
ð Send Telegram Files to Encode by /encode
ð I can Do Anything As you need for your encode
ð You can Customize the `FFMPEG` anytime via /setffmpeg Command
ð I am Filled with libfdk_aac Library of FFMPEG which is Best to Give HE-AAC Audio Quality !!
"""
        await e.reply(
            hp,
            buttons=[
                [Button.inline("Back â©", data="beck")],
            ],
        )
    except Exception as h:
        LOGS.info(h)
