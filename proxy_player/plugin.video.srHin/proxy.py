import requests
from bs4 import BeautifulSoup
import urllib.request

URL_POOL = ["https://free-proxy-list.net/"]
PROXY_POOL = []
DATA_SET = []
NEW_VID_URL_hin = "https://www.fifastop.com/newvideos.php"


def proxy_fetcher(url=URL_POOL[0]):
	res = requests.get(url)
	soup = BeautifulSoup(res.content, "html.parser")
	if "free-proxy-list.net" in url:
		count = 0
		proxy_table = soup.find("table", {"id": "proxylisttable"})
		proxy_row = proxy_table.findAll("tr")[1:]
		for pr in proxy_row:
			proxy_dict = {}
			count += 1
			single_proxy = [i for i in pr.strings]
			proxy_dict["IP"] = single_proxy[0]
			proxy_dict["Port"] = single_proxy[1]
			# proxy_dict["meta"] = [single_proxy[2], single_proxy[4], single_proxy[7]]
			proxy_dict["meta"] = single_proxy[2:]
			PROXY_POOL.append(proxy_dict)
			if count > 10:
				break
		return PROXY_POOL


def link_getter(url="https://fifastop.com"):
	# print(proxy_fetcher())
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	new_videos_ul = soup.find("ul", {"id":"pm-grid"})
	for item in new_videos_ul.find_all("li"):
		data_single = {}
		data_single["title"] = item.find_all("a")[1]["title"]
		data_single["link"] = item.find_all("a")[1]["href"]
		data_single["since_time"] = item.find("span", {"class": "pm-video-attr-since"}).text
		data_single["since_num_only"] = [int(s) for s in data_single["since_time"].split() if s.isdigit()]
		DATA_SET.append(data_single)
	return DATA_SET
	# new_videos = new_videos_ul.find_all("a", {'class': 'pm-title-link'}, href=True)


def get_playable_link(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	return soup.find_all("link", {"rel":"video_src"})[0]["href"]

if __name__ == "__main__":
	data_set = link_getter(NEW_VID_URL_hin)
	input = 9
	select = DATA_SET[input]['link']
	url = get_playable_link(select)
	# https://www.fifastop.com/uploads/videos/8d276515.mp4
	# https://www.fifastop.com/
	if url.startswith("http://video.fifastop.com/"):
		url = url.replace("http://video.", "https://www.")

	print(url)
	
