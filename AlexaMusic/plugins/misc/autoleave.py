# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import logging
import asyncio
from pyrogram.enums import ChatType
from pytgcalls.exceptions import NotInCallError, NoActiveGroupCall

import config
from AlexaMusic import app
from AlexaMusic.core.call import Alexa, autoend
from AlexaMusic.utils.database import (
    get_client,
    is_active_chat,
    is_autoend,
    set_loop
)

autoend = {}


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(config.AUTO_LEAVE_ASSISTANT_TIME):
            from AlexaMusic.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                try:
                    async for i in client.get_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001686672798
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(chat_id)
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while True:
        await asyncio.sleep(30)
        try:
            if not await is_autoend():
                continue
            member = []
            for chat_id in autoend.items():
                try:
                    ksk, me = await Alexa.vcmembers(chat_id)
                    ksk = ksk>1
                except NoActiveGroupCall:
                    continue
                except NotInCallError:
                    continue
                except:
                    ksk = False

                if not ksk and me:
                    await set_loop(chat_id, 0)
                    await Alexa.stop_stream(chat_id)
                    try:
                        await app.send_message(chat_id,"ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄʟᴇᴀʀᴇᴅ ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ sᴏɴɢs ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.")
                    except Exception as e:
                        logging.info(f"Error: {e}")
                    member.append(chat_id)
            autoend.pop(chat_id, None)
        except Exception as e:
            logging.info(f"Error: {e}")


asyncio.create_task(auto_end())
