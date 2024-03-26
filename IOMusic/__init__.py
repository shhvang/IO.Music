from IOMusic.core.bot import IO
from IOMusic.core.dir import dirr
from IOMusic.core.git import git
from IOMusic.core.userbot import Userbot
from IOMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = IO()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
