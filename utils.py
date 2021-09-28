import os, spotipy
from dotenv import load_dotenv
from discord.ext import commands
from spotipy.oauth2 import SpotifyClientCredentials
from random import randint

YOUTUBE_API_KEYS = 3
SPOTIFY_CREDENTIALS = {}
YOUTUBE_CREDENTIALS = []

client = commands.Bot(command_prefix="!", case_insensitive=True)
queue = {}


if os.path.isfile("./.env"):
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
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
    client_id = SPOTIFY_CREDENTIALS["id"],
    client_secret = SPOTIFY_CREDENTIALS["secret"]
))


def get_youtube_key():
    key_index = randint(0, YOUTUBE_API_KEYS - 1)
    return YOUTUBE_CREDENTIALS[key_index]

