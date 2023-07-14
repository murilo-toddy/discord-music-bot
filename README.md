# Discord Music Bot

A music bot that plays songs from Youtube or Spotify. Bot uses '!' as commands prefix, and a list of
all commands can be found using `!help`.


## Configuration

Data for bot configuration has to be specified as a `.env` file or by the use of environment
variables.

You must provide your discord bot token, your ID to a verified Spotify API account
and as many Youtube API keys as you wish. File formatting should be as follows:

```
DISCORD_TOKEN =
SPOTIFY_ID =
SPOTIFY_SECRET =
YOUTUBE_API_KEY1 = 
YOUTUBE_API_KEY2 = 
...
```

If you wish, you can also create a `cookies.txt` file containing cookie information from your browser.
This cookie authentification is used to remove age restriction from certain songs.

## Dependencies

This bot depends on various APIs and libraries that are specified in the `requirements.txt` file.
Also, you need to have `ffmpeg` installed in your machine.

## Execution

A makefile is present in this project to allow for container creation and execution in an easier manner.

To run the project use 

```bash
make run 
```

To run tests for the project use 

```bash
make test 
```

