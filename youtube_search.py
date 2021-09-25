import urllib.request
import re
import urllib.parse

def YoutubeSearch(url):
    urlBusca = urllib.parse.quote(url)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+urlBusca)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    UrlVideo ="https://www.youtube.com/watch?v=" + video_ids[0]

    Video_Identificator = {}

    Video_Identificator["url"] = UrlVideo
    Video_Identificator["id"] = video_ids[0]

    return Video_Identificator
