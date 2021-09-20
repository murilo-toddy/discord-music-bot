# from requests_html import AsyncHTMLSession
# from bs4 import BeautifulSoup as bs
# import nest_asyncio

# async def get_video_data(url):
# 	nest_asyncio.apply()
# 	session = AsyncHTMLSession()
# 	response = await session.get(url)

# 	await response.html.arender(sleep=1)
# 	soup = bs(response.html.html, "html.parser")

# 	video_info = {}

# 	video_info["url"] = url
# 	video_info["title"] = soup.find("meta", itemprop="name")["content"]
# 	video_info["views"] = soup.find("meta", itemprop="interactionCount")['content']
# 	video_info["published"] = soup.find("meta", itemprop="datePublished")['content']
# 	# video_info["duration"] = await soup.find("span", {"class": "ytp-time-duration"}).text

# 	return video_info


# # print(asyncio.run(get_video_data("https://www.youtube.com/watch?v=uHBaYkl3ZVQ")))

from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

part_string = 'contentDetails,statistics,snippet'
video_ids = 'H9154xIoYTA'

response = service.videos().list(
	part=part_string,
	id=video_ids
).execute()

pprint(response)