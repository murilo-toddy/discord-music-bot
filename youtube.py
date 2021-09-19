from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup as bs

async def get_video_data(url):
	session = AsyncHTMLSession()
	response = await session.get(url)

	response.html.arender(sleep=1)
	soup = bs(response.html.html, "html.parser")

	video_info = {}

	video_info["url"] = url
	video_info["title"] = soup.find("meta", itemprop="name")["content"]
	video_info["views"] = soup.find("meta", itemprop="interactionCount")['content']
	video_info["published"] = soup.find("meta", itemprop="datePublished")['content']
	#video_info["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text


	return video_info
