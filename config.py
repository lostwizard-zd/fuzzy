import os
import re

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


def _env(name: str, default=None, *, required: bool = False):
    value = os.getenv(name, default)
    if required and (value is None or str(value).strip() == ""):
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def _int_env(name: str, default=None, *, required: bool = False):
    value = _env(name, default, required=required)
    if value is None or str(value).strip() == "":
        if required:
            raise RuntimeError(f"Missing required environment variable: {name}")
        return None
    try:
        return int(str(value).strip())
    except ValueError as exc:
        raise RuntimeError(f"{name} must be an integer") from exc


def _bool_env(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on", "y"}


# Telegram application credentials
API_ID = _int_env("API_ID", required=True)
API_HASH = _env("API_HASH", required=True)
BOT_TOKEN = _env("BOT_TOKEN", required=True)

# Database / limits
MONGO_DB_URI = _env("MONGO_DB_URI", required=True)
DURATION_LIMIT_MIN = _int_env("DURATION_LIMIT", 60)
LOGGER_ID = _int_env("LOGGER_ID", required=True)

# Owner configuration. OWNER_IDS supports comma-separated IDs while OWNER_ID
# remains supported for backwards compatibility.
_owner_values = [
    item.strip()
    for item in _env("OWNER_IDS", "").split(",")
    if item.strip()
]
if not _owner_values:
    legacy_owner = _env("OWNER_ID", "")
    if legacy_owner:
        _owner_values = [legacy_owner]
OWNER_IDS = {int(item) for item in _owner_values if item.lstrip("-").isdigit()}
OWNER_ID = next(iter(OWNER_IDS), 0)

# Optional deployment/update integration
HEROKU_APP_NAME = _env("HEROKU_APP_NAME")
HEROKU_API_KEY = _env("HEROKU_API_KEY")
UPSTREAM_REPO = _env("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = _env("UPSTREAM_BRANCH", "main")
GIT_TOKEN = _env("GIT_TOKEN")

# Public/support links
SUPPORT_CHANNEL = _env("SUPPORT_CHANNEL", "https://t.me/")
SUPPORT_CHAT = _env("SUPPORT_CHAT", "https://t.me/")
ASSISTANT_SUPPORT_CHAT = _env("ASSISTANT_SUPPORT_CHAT", "")
AUTO_LEAVING_ASSISTANT = _bool_env("AUTO_LEAVING_ASSISTANT", False)

# Spotify is optional. Do not ship credentials in source control.
SPOTIFY_CLIENT_ID = _env("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = _env("SPOTIFY_CLIENT_SECRET", "")

PLAYLIST_FETCH_LIMIT = _int_env("PLAYLIST_FETCH_LIMIT", 25)
TG_AUDIO_FILESIZE_LIMIT = _int_env("TG_AUDIO_FILESIZE_LIMIT", 104857600)
TG_VIDEO_FILESIZE_LIMIT = _int_env("TG_VIDEO_FILESIZE_LIMIT", 1073741824)

# Assistant sessions. At least STRING_SESSION is required by the startup checks.
STRING1 = _env("STRING_SESSION")
STRING2 = _env("STRING_SESSION2")
STRING3 = _env("STRING_SESSION3")
STRING4 = _env("STRING_SESSION4")
STRING5 = _env("STRING_SESSION5")

# Optional yt-dlp cookies. For large cookie files, split the base64 value across
# YTDLP_COOKIES_B64_1, _2, ... and the bot will concatenate them in order.
YTDLP_COOKIES_B64 = _env("YTDLP_COOKIES_B64", "")
YTDLP_COOKIES_B64_PARTS = [
    os.getenv(f"YTDLP_COOKIES_B64_{i}", "")
    for i in range(1, 21)
]
YTDLP_COOKIES_B64_PARTS = [part.strip() for part in YTDLP_COOKIES_B64_PARTS if part.strip()]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = _env(
    "START_IMG_URL", "https://te.legra.ph/file/52e4add1f5b427f41f2e4.jpg"
)
PING_IMG_URL = _env(
    "PING_IMG_URL", "https://te.legra.ph/file/0381639bbd5f1ee1c190b.jpg"
)
PLAYLIST_IMG_URL = _env(
    "PLAYLIST_IMG_URL", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
)
STATS_IMG_URL = _env(
    "STATS_IMG_URL", "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
)
TELEGRAM_AUDIO_URL = _env(
    "TELEGRAM_AUDIO_URL", "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
)
TELEGRAM_VIDEO_URL = _env(
    "TELEGRAM_VIDEO_URL", "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
)
STREAM_IMG_URL = _env(
    "STREAM_IMG_URL", "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
)
SOUNCLOUD_IMG_URL = _env(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
)
YOUTUBE_IMG_URL = _env(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
)
SPOTIFY_ARTIST_IMG_URL = _env(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
)
SPOTIFY_ALBUM_IMG_URL = _env(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = _env(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

for _url_name in ("SUPPORT_CHANNEL", "SUPPORT_CHAT"):
    _url = globals()[_url_name]
    if _url and not re.match(r"(?:http|https)://", _url):
        raise RuntimeError(
            f"{_url_name} must start with http:// or https://"
        )
