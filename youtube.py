from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

def get_video_data(url):
	session = HTMLSession()
	response = session.get(url)

	response.html.render(sleep=1)
	soup = bs(response.html.html, "html.parser")

	video_info = {}

	video_info["title"] = soup.find("meta", itemprop="name")["content"]
	video_info["views"] = soup.find("meta", itemprop="interactionCount")['content']
	video_info["published"] = soup.find("meta", itemprop="datePublished")['content']
	video_info["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text

	return video_info
