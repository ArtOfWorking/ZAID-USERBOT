import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "10779850")) #optional
API_HASH = getenv("API_HASH", "a41b332506dc52820be5182b90e75c58") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1918390383 1927696336").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "6131397272:AAG25oOhUYw0YRmEL-ZSes457DTXihh5R3E")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ArtOfWorking/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAtCr3wdszu1udwBbyDsQDM23Bgy2cflMq09XG4zJHql6RBDO94ZTZTxJ20ngLNnM7KI9fkkomqw5zi1fnGYCc9xM2LblRzDGTFpPY6xhdlcsQ2lA4jVw_lqcF2pfjDvuY8PY5e-jmlWtsEAGq979xbJ3wPjBPMGYlfqexVyIk3x9eBfNRGWQ-z1eRHzxqwXKkpc_xPaKf367yHLND_9H7ADvqGKYrAtyPkEbLvKk8OlYBnhIQzbplypdSgKWMRuSd6_596mHKYNfl2l-I4XnbmzpQ4VFv9kRtaEAtXPJfnIFEAxwJaTxi2cF7A-dNosd5QdGY74-AcLkYlU9mjTWpZwAAAAByWFBvAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
