import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '18032586'))
API_HASH = environ.get('API_HASH', '4407d04c3f4f0fe56e6d03a41f64d71c')
BOT_TOKEN = environ.get('BOT_TOKEN', "2053611998:AAH0p4pCpFTaL4sX6p1QS05EcFCW6sGDWwU")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/1d4e26fd8f17da33a5a80.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/1d4e26fd8f17da33a5a80.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/1d4e26fd8f17da33a5a80.jpg")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/1d4e26fd8f17da33a5a80.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1232136108').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001760527515').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1001410981392')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sk16:sk16@bot5.jvjax.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "bot5")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'tg_world')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/requestbox1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/requestbox1official')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/helpsarthak_bot')
MSG_ALRT = environ.get('MSG_ALRT', 'Buy Premium For Direct Files')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', -1001491418577))
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', -1001485190065))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/rb1index')
HOW_DWLD_LINK = environ.get('HOW_DWLD_LINK', 'https://t.me/rb1bots/8')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001485190065))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', -1001485190065))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "@rb1official {file_name} \nsɪᴢᴇ : {file_size} \n\n┏➪[ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs](https://t.me/requestbox1official)</b> \n┠➤[ᴊᴏɪɴ ᴘʀᴇᴍɪᴜᴍ](https://t.me/rb1official)</b> \n┠〉〉〉[ᴅᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/know_sarthak16)</b> \n┠➤[ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs](https://t.me/rb1bots)</b> \n┖➪[ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ](https://t.me/requestbox1)</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "@rb1official <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [Movie Updates](https://t.me/rb1official)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>{mention}'s Qᴜᴇʀʏ ☞ <code>{query}</code>\n\n<b>🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rb1bots</b>")
CYNITE_IMDB_TEMPLATE = environ.get("KD_IMDB_TEMPLATE", "🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rb1bots")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001485190065')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Auto Delete , Filter & Auto Filter
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
MAUTO_DELETE = is_enabled((environ.get('MAUTO_DELETE', "True")), True)

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
SPL_DELETE_TIME = int(environ.get('SPL_DELETE_TIME', 15))

# URL SHORTNER

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'shorturllink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'd2ac0cef4a3d14ea75b37aa70c75a4acee726479')

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
