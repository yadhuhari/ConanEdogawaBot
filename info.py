import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
𝙷𝚎𝚢 𝚝𝚑𝚎𝚛𝚎 👋,

𝙸 𝚊𝚖 𝙲𝚘𝚗𝚊𝚗 𝙴𝚍𝚘𝚐𝚊𝚠𝚊, 𝙸 𝚌𝚊𝚗 𝚙𝚛𝚘𝚟𝚒𝚍𝚎 𝙷𝚘𝚕𝚕𝚢𝚠𝚘𝚘𝚍 𝙼𝚊𝚕𝚊𝚢𝚊𝚕𝚊𝚖 𝙳𝚞𝚋𝚋𝚎𝚍 𝙼𝚘𝚟𝚒𝚎𝚜 𝚏𝚘𝚛 𝚈𝚘𝚞. 𝙹𝚞𝚜𝚝 𝚜𝚎𝚊𝚛𝚌𝚑 𝚝𝚑𝚎 𝚖𝚘𝚟𝚒𝚎 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 & 𝚎𝚗𝚓𝚘𝚢 😍
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
