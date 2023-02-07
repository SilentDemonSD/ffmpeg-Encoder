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

import asyncio
import os
import signal

import psutil
from telethon import errors

from bot import FFMPEG, LOG_FILE

from . import *
from .config import *
from .worker import *

WORKING = []
QUEUE = {}
OK = {}

uptime = dt.now()
os.system(f"wget {THUMB} -O thumb.jpg")


if not os.path.isdir("downloads/"):
    os.mkdir("downloads/")
if not os.path.isdir("encode/"):
    os.mkdir("encode/")
if not os.path.isdir("thumb/"):
    os.mkdir("thumb/")


def stdr(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)
    if len(str(hours)) == 1:
        hours = "0" + str(hours)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    dur = (
        ((str(hours) + ":") if hours else "00:")
        + ((str(minutes) + ":") if minutes else "00:")
        + ((str(seconds)) if seconds else "")
    )
    return dur


def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]


def hbs(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "B", 1: "K", 2: "M", 3: "G", 4: "T", 5: "P"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


No_Flood = {}


async def progress(current, total, event, start, type_of_ps, file=None):
    now = time.time()
    if No_Flood.get(event.chat_id):
        if No_Flood[event.chat_id].get(event.id):
            if (now - No_Flood[event.chat_id][event.id]) < 1.1:
                return
        else:
            No_Flood[event.chat_id].update({event.id: now})
    else:
        No_Flood.update({event.chat_id: {event.id: now}})
    diff = time.time() - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = round((total - current) / speed) * 1000
        progress_str = "`[{0}{1}] {2}%`\n\n".format(
            "".join(["◆" for i in range(math.floor(percentage / 5))]),
            "".join(["◇" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )
        tmp = (
            progress_str
            + "`{0} of {1}`\n\n`✦ 🚀 Speed: {2}/s`\n\n`✦ ⏳ ETA: {3}`\n\n".format(
                hbs(current),
                hbs(total),
                hbs(speed),
                ts(time_to_completion),
            )
        )
        try:
            if file:
                await event.edit(
                    "`✦ {}`\n\n`File Name: {}`\n\n{}".format(type_of_ps, file, tmp)
                )
            else:
                await event.edit("`✦ {}`\n\n{}".format(type_of_ps, tmp))
        except errors.EditMessageRequest as e:
            LOGS.info("Flood wait for ", e.seconds)
            await asyncio.sleep(15)


async def sysinfo(event):
    try:
        systemm = "neofetch --stdout"
        fetch = await asyncio.create_subprocess_shell(
            systemm,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())
        await event.reply(f"**{result}**")
    except FileNotFoundError:

        await event.reply("**Install neofetch first**")


async def info(file, event):
    process = subprocess.Popen(
        ["mediainfo", file, "--Output=HTML"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, stderr = process.communicate()
    out = stdout.decode()
    client = TelegraphPoster(use_api=True)
    client.create_api_token("Mediainfo")
    page = client.post(
        title="FX-EnCodes",
        author=((await event.client.get_me()).first_name),
        author_url=f"https://t.me/{((await event.client.get_me()).username)}",
        text=out,
    )
    return page["url"]


def code(data):
    OK.update({len(OK): data})
    return str(len(OK) - 1)


def decode(key):
    if OK.get(int(key)):
        return OK[int(key)]
    return


async def skip(e):
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, id = wh.split(";")
    try:
        if QUEUE.get(int(id)):
            WORKING.clear()
            QUEUE.pop(int(id))
        await e.delete()
        # os.remove(dl)
        # os.remove(out)
        # Lets kill ffmpeg else it will run in memory even after deleting
        # input.
        for proc in psutil.process_iter():
            processName = proc.name()
            processID = proc.pid
            print(processName, " - ", processID)
            if processName == "ffmpeg":
                os.kill(processID, signal.SIGKILL)
    except Exception as er:
        LOGS.info(er)
    except BaseException:
        pass
    return


async def renew(e):
    try:
        WORKING.clear()
        QUEUE.clear()
        os.system("rm -rf downloads/*")
        os.system("rm -rf encode/*")
        for proc in psutil.process_iter():
            processName = proc.name()
            processID = proc.pid
            print(processName, " - ", processID)
            if processName == "ffmpeg":
                os.kill(processID, signal.SIGKILL)
        await e.reply(
            "✅ `Successfully Cleared` ✅\n\n**>>Cleared Queued, Working Files and Cached Downloads!**"
        )
    except Exception as er:
        LOGS.info(er)

    return


async def setcode(e):
    """/setffmpeg Command"""
    ffmpeg = e.text.split(" ", maxsplit=1)[1]
    global FFMPEG
    FFMPEG.clear()
    FFMPEG.insert(0, ffmpeg)
    await e.reply(f"**Changed FFMPEG Code to**\n\n`{FFMPEG[0]}`")
    return


async def getcode(e):
    await e.reply(f"**Your Current FFMPEG Code is**\n\n`{FFMPEG[0]}`")
    return


async def getlogs(e):
    if str(e.chat_id) not in AUTH_CHATS:
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return
    await e.client.send_file(e.chat_id, file=LOG_FILE, force_document=True)


async def getthumb(e):
    await e.client.send_file(
        e.chat_id,
        file="/bot/thumb.jpg",
        force_document=False,
        caption="**Bot's Current Thumbnail.**",
    )


async def clearqueue(e):
    # if str(e.sender_id) not in SUDO_USERS and event.sender_id != CREATOR:
    # return
    QUEUE.clear()
    await e.reply("**Cleared All Queued Files!**")
    return


async def fast_download(e, download_url, filename=None):
    try:

        def progress_callback(d, t):
            return (
                f"📥 `Downloading...` from [link]({download_url}) 📥 :",
                """f"progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                     progress(
                        d,
                        t,
                        e,
                        time.time(),
                        f"📥 `Downloading...` from [link]({download_url}) 📥 :",
                    )
                ),""",
            )

    except errors.FloodWaitError as e:
        LOGS.info("Flood wait for ", e.seconds)
        await asyncio.sleep(e.x)

    async def _maybe_await(value):
        if inspect.isawaitable(value):
            return await value
        else:
            return value

    async with aiohttp.ClientSession() as session:
        async with session.get(download_url, timeout=None) as response:
            if not filename:
                filename = download_url.rpartition("/")[-1]
            filename = os.path.join("downloads", filename)
            total_size = int(response.headers.get("content-length", 0)) or None
            downloaded_size = 0
            with open(filename, "wb") as f:
                async for chunk in response.content.iter_chunked(1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        await _maybe_await(
                            progress_callback(downloaded_size, total_size)
                        )
            return filename
