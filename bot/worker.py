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

import urllib.parse

from . import *
from .config import *
from .FastTelethon import download_file, upload_file
from .funcn import *
from .funcn import FFMPEG


async def stats(e):
    try:
        wah = e.pattern_match.group(1).decode("UTF-8")
        wh = decode(wah)
        out, dl, id = wh.split(";")
        ot = hbs(int(Path(out).stat().st_size))
        ov = hbs(int(Path(dl).stat().st_size))
        cpuu = psutil.cpu_percent(interval=0.5)
        ramm = psutil.virtual_memory().percent
        diskk = psutil.disk_usage("/").percent
        file_name = dl.replace("downloads/", "").replace("_", " ")
        ans = f"🗂 File Name 🗂 \n☛ {file_name}\n\n⚡Total Size:⚡\n☛ {ov}\n\n⚡Compressed Size:⚡\n☛ {ot}\n\nCPU: {cpuu}% RAM: {ramm}% DISK: {diskk}%"
        await e.answer(ans, cache_time=0, alert=True)
    except Exception as er:
        LOGS.info(er)
        await e.answer(
            "🙄 Someting Went Wrong !! 🤔\nMaybe Bot was 🔄 Restarted 🔄 .",
            cache_time=0,
            alert=True,
        )


async def dl_link(event):
    # if event.is_private:
    # return
    link, name = "", ""
    try:
        link = event.text.split()[1]
        name = event.text.split()[2]
    except BaseException:
        pass
    capp = name
    if not link:
        await event.reply("`Send Link along with /dl`")
        return
    if WORKING or QUEUE:
        f = event.message.id
        sen = event.chat_id
        QUEUE.update({link: (name, sen, f)})
        return await event.reply(f"Aᴅᴅᴇᴅ Iɴ Qᴜᴇᴜᴇ !!\n ⚡ Lɪɴᴋ : [Click Here]({link})")
    WORKING.append(1)
    s = dt.now()
    xxx = await event.reply("📥 `Downloading...` 📥")
    try:
        dl = await fast_download(xxx, link, name)
    except Exception as er:
        WORKING.clear()
        LOGS.info(er)
        return
    es = dt.now()
    kk = dl.split("/")[-1]
    aa = kk.split(".")[-1]
    rr = "encode"
    bb = kk.replace(f".{aa}", "~FX.mkv")
    bb = urllib.parse.unquote(bb)
    out = f"{rr}/{bb}"
    thum = "thumb.jpg"
    dtime = ts(int((es - s).seconds) * 1000)
    hehe = f"{out};{dl};0"
    wah = code(hehe)
    nn = await xxx.edit(
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
            await xxx.edit(str(er) + "\n\n📮 **ERROR** 📮")
            WORKING.clear()
            os.remove(dl)
            return os.remove(out)
    except BaseException:
        pass
    if capp == "":
        cap = bb
    else:
        cap = capp
    ees = dt.now()
    ttt = time.time()
    await nn.delete()
    nnn = await event.reply("📤 `Uploading ...` 📤")
    with open(out, "rb") as f:
        ok = await upload_file(
            client=xxx.client,
            file=f,
            name=out,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, nnn, ttt, "📤 `Uploading ...` 📤")
            ),
        )
    ds = await xxx.client.send_file(
        xxx.chat_id,
        file=ok,
        caption=cap,
        force_document=True,
        thumb=thum,
        reply_to=event.message.id,
    )
    await nnn.delete()
    org = int(Path(dl).stat().st_size)
    com = int(Path(out).stat().st_size)
    pe = 100 - ((com / org) * 100)
    per = str(f"{pe:.2f}") + "%"
    eees = dt.now()
    x = dtime
    xx = ts(int((ees - es).seconds) * 1000)
    up = ts(int((eees - ees).seconds) * 1000)
    a1 = await info(dl, xxx)
    a2 = await info(out, xxx)
    dk = await ds.reply(
        f"Original Size : {hbs(org)}\nCompressed Size : {hbs(com)}\nCompressed Percentage : {per}\n\nMediainfo: [Before]({a1})//[After]({a2})\n\nDownloaded in {x}\nCompressed in {xx}\nUploaded in {up}",
        link_preview=False,
    )
    os.remove(dl)
    os.remove(out)
    WORKING.clear()


async def encod(event):
    try:
        # if not event.is_private:
        # return
        if not event.is_reply:
            await event.reply("`Reply to Media to Start Compress !!`")
            return
            uni = await event.get_reply_message()
        if hasattr(uni.media, "document"):
            if not uni.media.document.mime_type.startswith(
                ("video", "application/octet-stream")
            ):
                return
        else:
            return
        try:
            oc = event.fwd_from.from_id.user_id
            occ = (await event.client.get_me()).id
            if oc == occ:
                return await event.reply("This Video File is already Compressed 😑😑.")
        except BaseException:
            pass
        if WORKING or QUEUE:
            xxx = await event.reply("♨️ Aᴅᴅᴇᴅ Iɴ Qᴜᴇᴜᴇ ♨️!!")
            # id = pack_bot_file_id(event.media)
            doc = uni.media.document
            if doc.id in list(QUEUE.keys()):
                return await xxx.edit("🗜 THIS FILE ALREADY IN QUEUE 🗜")
            nam = ""
            try:
                nam = event.text.split()[1]
            except BaseException:
                pass
            if not nam:
                name = uni.file.name
            else:
                name = nam
                if not name:
                    name = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                QUEUE.update({doc.id: [name, doc]})
                return await xxx.edit(
                    "♨️ Aᴅᴅᴇᴅ Iɴ Qᴜᴇᴜᴇ ♨️!! \n\n `Please Wait` , Compress will Start Soon ..."
                )
        WORKING.append(1)
        xxx = await event.reply("📥 `Downloading ...` 📥")
        s = dt.now()
        ttt = time.time()
        dir = f"downloads/"
        try:
            if hasattr(event.media, "document"):
                file = event.media.document
                filename = event.file.name
                if not filename:
                    filename = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                dl = dir + filename
                with open(dl, "wb") as f:
                    ok = await download_file(
                        client=event.client,
                        location=file,
                        out=f,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d,
                                t,
                                xxx,
                                ttt,
                                "📥 `Downloading ...` 📥",
                            )
                        ),
                    )
            else:
                dl = await event.client.download_media(
                    event.media,
                    dir,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, xxx, ttt, "📥 `Downloading ...` 📥")
                    ),
                )
        except Exception as er:
            WORKING.clear()
            LOGS.info(er)
            return os.remove(dl)
        es = dt.now()
        kk = dl.split("/")[-1]
        aa = kk.split(".")[-1]
        rr = f"encode"
        bb = kk.replace(f".{aa}", " [Encoded].mkv")
        out = f"{rr}/{bb}"
        thum = "thumb.jpg"
        dtime = ts(int((es - s).seconds) * 1000)
        e = xxx
        hehe = f"{out};{dl};0"
        wah = code(hehe)
        nn = await e.edit(
            "`Your File is Now Getting Compressed :` \n\n ©FX-EnCodes",
            buttons=[
                [Button.inline("📊 Check Stats 📊", data=f"stats{wah}")],
                [Button.inline("📮 Cancel 📮", data=f"skip{wah}")],
            ],
        )
        cmd = FFMPEG.format(dl, out)
        process = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        er = stderr.decode()
        try:
            if er:
                await e.edit(str(er) + "\n\n**ERROR** Contact @danish_00")
                WORKING.clear()
                os.remove(dl)
                return os.remove(out)
        except BaseException:
            pass
        ees = dt.now()
        ttt = time.time()
        await nn.delete()
        nnn = await e.client.send_message(e.chat_id, "📤 `Uploading ...` 📤")
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
            e.chat_id, file=ok, caption=name, force_document=True, thumb=thum
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
            f"Original File Size : {hbs(org)}\nEncoded File Size : {hbs(com)}\nEncoded File Percentage : {per}\n\nGet Mediainfo here : [Before]({a1})//[After]({a2})\n\nDownloaded in {x}\nEncoded File in {xx}\nUploaded in {xxx}",
            link_preview=False,
        )
        os.remove(dl)
        os.remove(out)
        WORKING.clear()
    except BaseException as er:
        LOGS.info(er)
        WORKING.clear()
