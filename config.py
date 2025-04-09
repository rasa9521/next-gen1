import os

API_ID = os.environ.get("API_ID", "12475131")

API_HASH = os.environ.get("API_HASH", "719171e38be5a1f500613837b79c536f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7673015455:AAFzEP1Zy1EV2BGa8KhEYjoQ1ET0qHr2g4g")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1714266885))

LOG = -1002542634912,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[7827463899]
    for x in (os.environ.get("ADMINS", "1714266885").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
