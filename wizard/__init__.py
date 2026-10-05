from wizard.core.bot import WizardBot
from wizard.core.dir import dirr
from wizard.core.git import git
from wizard.core.userbot import Userbot
from wizard.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

nand = WizardBot()
userbot = Userbot()

from .platforms import *  # noqa: E402,F403

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
