# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777

from os import path, getenv, environ

class Config:
    API_ID = int(getenv("API_ID", "29171167"))
    API_HASH = getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    
    CHANNEL_IDS = list(map(int, getenv("CHANNEL_IDS", "-1001959922658,-1002470391435,-1002433552221, -1002252585703").split(",")))
    
    REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
    
    ADMINS = list(map(int, getenv("ADMINS", "7251898668 1337857036").split()))
    DATABASE_URI = getenv("DATABASE_URI", "")

    LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1002190352334")) 


START_IMG = (environ.get('START_IMG', 'https://graph.org/file/2518d4eb8c88f8f669f4c.jpg https://graph.org/file/d6d9d9b8d2dc779c49572.jpg https://graph.org/file/4b04eaad1e75e13e6dc08.jpg https://graph.org/file/05066f124a4ac500f8d91.jpg https://graph.org/file/2c64ed483c8fcf2bab7dd.jpg')).split()


class temp(object):    
    U_NAME = None
    B_NAME = None
      
Spidey = Config()

# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777
