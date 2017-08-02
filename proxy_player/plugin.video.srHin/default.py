import xbmc
import xbmcgui
import requests
from bs4 import BeautifulSoup

ADDON_ID = "plugin.video.srHin"
PLUGIN_URL = "plugin://" + ADDON_ID + "/"

URL_POOL = ["https://free-proxy-list.net/"]
# PROXY_POOL = []
URL_hin = "https://www.fifastop.com/"
NEW_VID_URL_hin = URL_hin + "newvideos.php?&page="
SEARCH_QUERY = URL_hin + "search.php?keywords=00000" + "&video-id="
RSS = URL_hin + "rss.php"  # xml content available at url


def main_list(name, link, since_time, back_url=None, nextPageToken=1, thumb=None, isFolder=False):
	xbmc.log('IN FUN=main_list()......', 2)  # log : NOTICE
	# xbmc.log('name : ' + str(name), 2)  # log : NOTICE
	u = PLUGIN_URL
	u += "?name=" + name
	if not thumb:
		thumb = xbmc.translatePath("special://home/addons/{}/icon.png".format(ADDON_ID))
	u += "&thumb=" + urllib.quote_plus(str(thumb))
	u += "&action=" + str(since_time)
	u += "&link=" + str(link)
	u += "&back_url=" + str(back_url)
	nextPageToken = nextPageToken + 1
	u += "&nextPageToken=" + str(nextPageToken)
	xbmc.log('url ..........................: ' + urllib.unquote_plus(str(u)), 2)  # log : NOTICE
	list_name = "{} ([B][COLOR lightseagreen]{}[/COLOR lightseagreen][/B])".format(name, since_time)
	liz = xbmcgui.ListItem(label=name, iconImage="", thumbnailImage=urllib.unquote_plus(thumb))
	liz.setInfo(type="video", infoLabels={"label": name, "title": name})
	liz.addContextMenuItems([('Refresh', 'Container.Refresh')])
	# liz.setArt({'poster': thumb})
	if not link.endswith(".mp4"):
		isFolder = True
	xbmcplugin.addDirectoryItem(abs(int(sys.argv[1])), u, liz, isFolder)
	xbmcplugin.addDirectoryItem(handle=abs(int(sys.argv[1])), url='{0}?nextPageToken={1}'.format(PLUGIN_URL, nextPageToken), listitem=xbmcgui.ListItem(label='Next Page >>>'), isFolder=True)


def link_getter(url=NEW_VID_URL_hin,page=1):
	# print(proxy_fetcher())
	response = requests.get(url+str(page))
	soup = BeautifulSoup(response.content, "html.parser")
	new_videos_ul = soup.find("ul", {"id":"pm-grid"})
	single_page_set = []
	for item in new_videos_ul.find_all("li"):
		data_single = {}
		title = data_single["title"] = item.find_all("a")[1]["title"]
		link = data_single["link"] = item.find_all("a")[1]["href"]
		since_time = data_single["since_time"] = item.find("span", {"class": "pm-video-attr-since"}).text
		since_num_only = data_single["since_num_only"] = [int(s) for s in data_single["since_time"].split() if s.isdigit()][0]
		single_page_set.append(data_single)
	return single_page_set
	# new_videos = new_videos_ul.find_all("a", {'class': 'pm-title-link'}, href=True)


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


def get_playable_link(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	url = soup.find_all("link", {"rel":"video_src"})[0]["href"]
	if url.startswith("http://video.fifastop.com/"):
		url = url.replace("http://video.", "https://www.")
	return url


def show_list(flag=0, page=1, s_link=None):
	if flag == 0:
		xbmc.log(">> flag 0", 2)
		data_set = link_getter()
		title = data_single["title"]
		link = data_single["link"]
		since_time = data_single["since_time"]
		since_num_only = data_single["since_num_only"]
		main_list(name=title, link=link, since_time=since_time, back_url=URL_hin)
	elif flag == 1:
		xbmc.log(">> flag 1", 2)
		play_link = get_playable_link(s_link)
		if play_link.endswith(".mp4"):
			xbmc.Player().play(play_link)


def main():
	param = {}
	paramstring = sys.argv[2]
	if len(paramstring) >= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if params[len(params) - 1] == '/':
			params = params[0:len(params) - 2]
		pairsofparams = cleanedparams.split('&')
		# param = {}
		for i in range(len(pairsofparams)):
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]

	if param:
		xbmc.log("> In param if", 2)
		xbmc.log("> In param : params==> {}".format(param), 2)
		if "link" in param:
			if param["link"].endswith(".mp4"):
				xbmc.log("> In param : playing", 2)
				xbmc.Player().play(param["link"])
			else:
				xbmc.log("> In param : listing", 2)
				show_list(param["link"], param["nextPageToken"])
	else:
		xbmc.log("> In param else", 2)
		show_list()


if __name__ == "__main__":
	main()
	# data_set = link_getter(NEW_VID_URL_hin)
	xbmcplugin.endOfDirectory(_handle,  cacheToDisc=False)
