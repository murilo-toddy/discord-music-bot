import pafy, discord
from youtube_dl import YoutubeDL

def download_song(url):
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    print(video.title)

    bestaudio.download()



def search_yt(item):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try: 
            info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
        except Exception: 
            return False

    return {'source': info['formats'][0]['url'], 'title': info['title']}

def play_next(self):
    if len(self.music_queue) > 0:
        self.is_playing = True

        #get the first url
        m_url = self.music_queue[0][0]['source']

        #remove the first element as you are currently playing it
        self.music_queue.pop(0)

        self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    else:
        self.is_playing = False

# infinite loop checking 
async def play_music(self):
    
    if len(self.music_queue) > 0:
        self.is_playing = True

        m_url = self.music_queue[0][0]['source']
        
        #try to connect to voice channel if you are not already connected

        if self.vc == "" or not self.vc.is_connected() or self.vc == None:
            self.vc = await self.music_queue[0][1].connect()
        else:
            await self.vc.move_to(self.music_queue[0][1])
        
        print(self.music_queue)
        #remove the first element as you are currently playing it
        self.music_queue.pop(0)

        self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    else:
        self.is_playing = False



