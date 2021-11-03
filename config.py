import os, spotipy
from data_structure import Bot
from dotenv import load_dotenv
from discord.ext import commands, tasks
from spotipy.oauth2 import SpotifyClientCredentials
from discord_slash import SlashCommand, SlashContext

YOUTUBE_API_KEYS = 9
YOUTUBE_CREDENTIALS = []
SPOTIFY_CREDENTIALS = {}
CURRENT_KEY_INDEX = -1

client = commands.Bot(command_prefix=">", case_insensitive=True, help_command=None)
slash = SlashCommand(client, sync_commands=True)
bot = Bot()


if os.path.isfile("./.env"):
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN_TODBOT")
    SPOTIFY_CREDENTIALS["id"] = os.getenv("SPOTIFY_ID")
    SPOTIFY_CREDENTIALS["secret"] = os.getenv("SPOTIFY_SECRET")
    for i in range(1, YOUTUBE_API_KEYS + 1):
        YOUTUBE_CREDENTIALS.append(os.getenv("YOUTUBE_API_KEY" + str(i)))
    
else:
    TOKEN = os.environ["DISCORD_TOKEN"]
    SPOTIFY_CREDENTIALS["id"] = os.environ["SPOTIFY_ID"]
    SPOTIFY_CREDENTIALS["secret"] = os.environ["SPOTIFY_SECRET"]
    for i in range(1, YOUTUBE_API_KEYS + 1):
        YOUTUBE_CREDENTIALS.append(os.environ["YOUTUBE_API_KEY" + str(i)]) 


spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CREDENTIALS["id"],
    client_secret=SPOTIFY_CREDENTIALS["secret"]
))


def get_youtube_key(): 
    global CURRENT_KEY_INDEX
    CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % YOUTUBE_API_KEYS
    return YOUTUBE_CREDENTIALS[CURRENT_KEY_INDEX]
