from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup as bs
import nest_asyncio

async def get_video_data(url):
	nest_asyncio.apply()
	session = AsyncHTMLSession()
	response = await session.get(url)

	await response.html.arender(sleep=1)
	soup = bs(response.html.html, "html.parser")

	video_info = {}

	video_info["url"] = url
	video_info["title"] = soup.find("meta", itemprop="name")["content"]
	video_info["views"] = soup.find("meta", itemprop="interactionCount")['content']
	video_info["published"] = soup.find("meta", itemprop="datePublished")['content']
	video_info["duration"] = await soup.find("span", {"class": "ytp-time-duration"}).text

	return video_info


# print(asyncio.run(get_video_data("https://www.youtube.com/watch?v=uHBaYkl3ZVQ")))