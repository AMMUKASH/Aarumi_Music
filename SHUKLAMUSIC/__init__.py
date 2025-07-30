from RAKSHAKMUSIC.core.bot import RAKSHAK
from RAKSHAKMUSIC.core.dir import dirr
from RAKSHAKMUSIC.core.git import git
from RAKSHAKMUSIC.core.userbot import Userbot
from RAKSHAKMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAKSHAK()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "ll_DRAGON_MUSIC_BOT"  # connect music api key "Dont change it"
