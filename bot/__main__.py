#    This file is part of the Compressor distribution.
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
# License can be found in
# <https://github.com/1Danish-00/CompressorQueue/blob/main/License> .
import urllib.parse

from . import *
from .config import *
from .devtools import *
from .FastTelethon import *

LOGS.info("Starting to Run . . .")


######## Connect ########


try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as er:
    LOGS.info(er)


####### GENERAL COMMANDS ########


@bot.on(events.NewMessage(pattern=f"/{START_CMD}"))
async def _(e):
    await start(e)


@bot.on(events.NewMessage(pattern=f"/{SET_FFMPEG}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await setcode(e)


@bot.on(events.NewMessage(pattern=f"/{GET_FFMPEG}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await getcode(e)


@bot.on(events.NewMessage(pattern=f"/{PING_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await up(e)


@bot.on(events.NewMessage(pattern=f"/{HELP_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await help(e)


@bot.on(events.NewMessage(pattern=f"/{LOG_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await getlogs(e)


@bot.on(events.NewMessage(pattern=f"/{DL_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await dl_link(e)


@bot.on(events.NewMessage(pattern=f"/{ENCODE_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await encod(e)


@bot.on(events.NewMessage(pattern=f"/{USAGE_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    total, used, free = shutil.disk_usage(".")
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    upload = hbs(psutil.net_io_counters().bytes_sent)
    down = hbs(psutil.net_io_counters().bytes_recv)
    TOTAL = hbs(total)
    USED = hbs(used)
    FREE = hbs(free)
    await e.reply(
        "**TOTAL DISK SPACE**: `{}`\n**USED**: `{}`\n**FREE**: {}\n**UPlOAD**: `{}`\n**DOWNLOAD**: `{}`\n**CPU**: `{}%`\n**RAM**: `{}%`\n**DISK**: `{}%`".format(
            TOTAL,
            USED,
            FREE,
            upload,
            down,
            cpuUsage,
            memory,
            disk,
        )
    )


@bot.on(events.NewMessage(pattern=f"/{SHOW_THUMB_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await getthumb(e)


@bot.on(events.NewMessage(pattern=f"/{SAVE_THUMB_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    imag = await e.get_reply_message()
    if not imag.photo:
        return e.reply("`Reply to a Custom Thumbnail`")
    os.system("rm thumb.jpg")
    await e.client.download_media(imag.media, file="/bot/thumb.jpg")
    await e.reply("**Thumbnail Saved Successfully.**")


@bot.on(events.NewMessage(pattern=f"/{SYSTEM_INFO}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await sysinfo(e)


@bot.on(events.NewMessage(pattern=f"/{RENEW_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await renew(e)


@bot.on(events.NewMessage(pattern=f"/{CLEAR_CMD}"))
async def _(e):
    if str(e.chat_id) not in AUTH_CHATS:
        LOGS.warning("Chat Not Found !!")
        if str(e.sender_id) not in SUDO_USERS and str(e.sender_id) != CREATOR:
            return e.reply(
                "**♨️ Sorry ♨️\n>> You aren't an Authorised User to Use Me .\n>> Become Authorised First .**"
            )
    await clearqueue(e)


######## Callback Data #########


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)


########## Direct ###########


@bot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)


@bot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


########## AUTO ###########


# @bot.on(events.NewMessage(incoming=True))
# async def _(e):
# await encod(e)


async def something():
    for i in itertools.count():
        try:
            if not WORKING and QUEUE:
                # user = int(SUDO_USERS.split()[0])
                chatt = QUEUE[list(QUEUE.keys())[0]][1]
                di = QUEUE[list(QUEUE.keys())[0]][2]
                e = await bot.send_message(
                    chatt, "📥 `Downloding Queue File` 📥", reply_to=di
                )
                # dl, file = QUEUE[list(QUEUE.keys())[0]]
                s = dt.now()
                try:
                    if isinstance(QUEUE[list(QUEUE.keys())[0]][1], int):
                        dl = await fast_download(
                            e, list(QUEUE.keys())[0], QUEUE[list(QUEUE.keys())[0]][0]
                        )
                    else:
                        dl, file = QUEUE[list(QUEUE.keys())[0]]
                        tt = time.time()
                        dl = "downloads/" + dl
                        with open(dl, "wb") as f:
                            ok = await download_file(
                                client=bot,
                                location=file,
                                out=f,
                                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                                    progress(
                                        d,
                                        t,
                                        e,
                                        tt,
                                        "📥 `Downloading...` 📥",
                                    )
                                ),
                            )
                except Exception as r:
                    LOGS.info(r)
                    WORKING.clear()
                    QUEUE.pop(list(QUEUE.keys())[0])
                cap = QUEUE[list(QUEUE.keys())[0]][0]
                es = dt.now()
                kk = dl.split("/")[-1]
                aa = kk.split(".")[-1]
                rr = "encode"
                bb = kk.replace(f".{aa}", "~FX.mkv")
                bb = urllib.parse.unquote(bb)
                out = f"{rr}/{bb}"
                thum = "thumb.jpg"
                dtime = ts(int((es - s).seconds) * 1000)
                hehe = f"{out};{dl};{list(QUEUE.keys())[0]}"
                wah = code(hehe)
                nn = await e.edit(
                    "`Your File is Now Getting Compressed :` \n\n ©FX-EnCodes",
                    buttons=[
                        [Button.inline("📊 Check Stats 📊", data=f"stats{wah}")],
                        [Button.inline("📮 Cancel 📮", data=f"skip{wah}")],
                    ],
                )
                cmd = FFMPEG[0].format(dl, out)
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                try:
                    if er:
                        await e.edit(str(er) + "\n\n📮 **ERROR** 📮")
                        QUEUE.pop(list(QUEUE.keys())[0])
                        os.remove(dl)
                        os.remove(out)
                        continue
                except BaseException:
                    pass
                ees = dt.now()
                ttt = time.time()
                await nn.delete()
                nnn = await e.client.send_message(
                    e.chat_id, "📤 `Uploading ...` 📤", reply_to=di
                )
                with open(out, "rb") as f:
                    ok = await upload_file(
                        client=e.client,
                        file=f,
                        name=out,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, nnn, ttt, "📤 `Uploading ...` 📤")
                        ),
                    )
                ds = await e.client.send_file(
                    e.chat_id,
                    file=ok,
                    caption=cap,
                    force_document=True,
                    thumb=thum,
                    reply_to=di,
                )
                await nnn.delete()
                org = int(Path(dl).stat().st_size)
                com = int(Path(out).stat().st_size)
                pe = 100 - ((com / org) * 100)
                per = str(f"{pe:.2f}") + "%"
                eees = dt.now()
                x = dtime
                xx = ts(int((ees - es).seconds) * 1000)
                xxx = ts(int((eees - ees).seconds) * 1000)
                a1 = await info(dl, e)
                a2 = await info(out, e)
                dk = await ds.reply(
                    f"Original File Size : {hbs(org)}\nEncoded File Size : {hbs(com)}\nEncoded File Percentage : {per}\n\nMediainfo: [Before]({a1})//[After]({a2})\n\nDownloaded in {x}\nCompressed in {xx}\nUploaded in {xxx}",
                    link_preview=False,
                )
                QUEUE.pop(list(QUEUE.keys())[0])
                WORKING.clear()
                os.remove(dl)
                os.remove(out)
            else:
                await asyncio.sleep(3)
        except Exception as err:
            LOGS.info(err)


########### Start ############

LOGS.info("Bot has Started!")
with bot:
    bot.loop.run_until_complete(something())
    bot.loop.run_forever()
