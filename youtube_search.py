import urllib.request, urllib.parse, re

def YoutubeSearch(urlPesquisa):

    search_url = urllib.parse.quote(urlPesquisa)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_url ="https://www.youtube.com/watch?v=" + video_ids[0]

    video_identifier = {}

    video_identifier["url"] = video_url
    video_identifier["id"] = video_ids[0]

    return video_identifier
