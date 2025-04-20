import os

API_ID = os.environ.get("API_ID", "27900743")

API_HASH = os.environ.get("API_HASH", "ebb06ea8d41420e60b29140dcee902fc"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8003649544:AAGoiThVN8KLJyKGsGf1BcfTsjDTrSmjFR8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7804396225))

LOG = -1002690129228,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[7804396225]
    for x in (os.environ.get("ADMINS", "7804396225").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
