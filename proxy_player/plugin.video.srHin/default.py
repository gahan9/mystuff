import xbmc
import xbmcgui
import xbmcplugin
import requests
import urllib
import json
from bs4 import BeautifulSoup
import sys


_handle = int(sys.argv[1])

ADDON_ID = "plugin.video.srHin"
PLUGIN_URL = "plugin://" + ADDON_ID + "/"

URL_POOL = ["https://free-proxy-list.net/"]
# PROXY_POOL = []
URL_hin = "https://www.fifastop.com/"
NEW_VID_URL_hin = URL_hin + "newvideos.php?&page="
SEARCH_QUERY = URL_hin + "search.php?keywords="  # ex: search.php?keywords=XXXXXXX&video-id=XXXXXXX
RSS = URL_hin + "rss.php"  # xml content available at url
VID_URL = URL_hin + "videos.php?vid="
POPULAR_VID_URL = URL_hin + "topvideos.php?&page="
MOST_WATCH = []
URL_hin_DICT = {"newvideos":NEW_VID_URL_hin, "popularvideos": POPULAR_VID_URL, "search":SEARCH_QUERY, "most_watch":MOST_WATCH}


def main_list(name, link, since_time="", action=None, back_url=None, nextPageToken=0, thumb=None, isFolder=False, isPlayable=False):
	xbmc.log('IN FUN=main_list()......', 2)  # log : NOTICE
	# xbmc.log('name : ' + str(name), 2)  # log : NOTICE
	u = PLUGIN_URL
	u += "?name=" + name
	if not thumb:
		thumb = xbmc.translatePath("special://home/addons/{}/icon.png".format(ADDON_ID))
	u += "&thumb=" + urllib.quote_plus(str(thumb))
	u += "&since_time=" + str(since_time)
	if since_time != "":
		vid = link.split("vid=")[-1]
		link = urllib.quote_plus(VID_URL + vid)
		xbmc.log(">>>> In if", 2)
		# xbmc.log(link, 2)
		action = "play"
		# isPlayable = True
	# action = "get_play_link" # for test
	u += "&action=" + str(action)
	u += "&link=" + str(link)
	u += "&back_url=" + str(back_url)
	nextPageToken = nextPageToken + 1
	u += "&nextPageToken=" + str(nextPageToken)
	try:
		if since_time:
			list_name = "{}  [B][COLOR lightseagreen]({})[/COLOR][/B]".format(name, since_time)
		else:
			list_name = name
		# list_name = name + "  ([B][COLOR red]" + since_time + "[/COLOR][/B])"
	except UnicodeEncodeError:
		list_name = name
	liz = xbmcgui.ListItem(label=list_name, iconImage="", thumbnailImage=urllib.unquote_plus(thumb))
	liz.setInfo(type="video", infoLabels={"label": name, "title": name})
	liz.addContextMenuItems([('Refresh', 'Container.Refresh')])
	# liz.setArt({'poster': thumb})
	# if not link.endswith(".mp4") or action != "play":
	# 	isFolder = True
	# xbmc.log('url ..........................: ' + urllib.unquote_plus(str(u)), 2)  # log : NOTICE
	xbmcplugin.addDirectoryItem(abs(int(sys.argv[1])), u, liz, isFolder, isPlayable)


def link_getter(url=NEW_VID_URL_hin, page=1):
	# if page != 1:
	# 	url = url + str(page)
	response = requests.get(url + str(page))
	soup = BeautifulSoup(response.content, "html.parser")
	single_page_set = []
	# if "newvideos.php" in url:
	# 	new_videos_ul = soup.find("ul", {"id":"pm-grid"})
	# 	vid_set = new_videos_ul.find_all("li")
	# elif "topvideos.php" in url:
	vid_set = soup.find_all("div", {"class":"pm-li-video"})

	for item in vid_set:
		data_single = {}
		title = data_single["title"] = item.find_all("a")[1]["title"]
		link = data_single["link"] = item.find_all("a")[1]["href"]
		since_time = data_single["since_time"] = item.find("span", {"class": "pm-video-attr-since"}).text
		since_num_only = data_single["since_num_only"] = [int(s) for s in data_single["since_time"].split() if s.isdigit()][0]
		single_page_set.append(data_single)
	# xbmc.log(">>> page_set : {}".format(single_page_set), 2)
	return single_page_set


def get_playable_link(url):
	response = requests.get(urllib.unquote_plus(url))
	soup = BeautifulSoup(response.content, "html.parser")
	url = soup.find_all("link", {"rel":"video_src"})[0]["href"]
	if url.startswith("http://video.fifastop.com/"):
		url = url.replace("http://video.", "https://www.")
	return url


def show_list(flag="main", page=1, s_link=None):
	if flag == "main":
		for main_items in URL_hin_DICT:
			if main_items == "newvideos":
				main_list(name="New Videos", link=URL_hin_DICT["newvideos"], action="new_list", isFolder=True)
			elif main_items == "popularvideos":
				main_list(name="Popular Videos", link=URL_hin_DICT["popularvideos"], action="popular_list", isFolder=True)
			elif main_items == "search":
				main_list(name="Search", link=SEARCH_QUERY, action="search", isFolder=True)
	elif flag == "new_list":
		xbmc.log(">> flag new_list", 2)
		data_set = link_getter(page=page)
		for data_single in data_set:
			title = data_single["title"]
			link = data_single["link"]
			since_time = data_single["since_time"]
			since_num_only = data_single["since_num_only"]
			main_list(name=title, link=link, since_time=since_time, back_url=URL_hin, action="play", isFolder=False)
		page = int(page) + 1
		xbmcplugin.addDirectoryItem(handle=abs(int(sys.argv[1])), url='{0}?link={1}&nextPageToken={2}&action={3}'.format(PLUGIN_URL, URL_hin_DICT["newvideos"], page, flag), listitem=xbmcgui.ListItem(label='Next Page >>>'), isFolder=True)
	elif flag=="popular_list":
		xbmc.log(">> flag popular_list", 2)
		data_set = link_getter(url=POPULAR_VID_URL, page=page)
		for data_single in data_set:
			title = data_single["title"]
			link = data_single["link"]
			since_time = data_single["since_time"]
			since_num_only = data_single["since_num_only"]
			main_list(name=title, link=link, since_time=since_time, back_url=URL_hin, action="play", isFolder=False)
		page = page + 1
		xbmcplugin.addDirectoryItem(handle=abs(int(sys.argv[1])), url='{0}?link={1}&nextPageToken={2}&action={3}'.format(PLUGIN_URL, URL_hin_DICT["popularvideos"], page, flag), listitem=xbmcgui.ListItem(label='Next Page >>>'), isFolder=True)
	elif flag == "search":
		search_string = xbmcgui.Dialog().input("Enter Search String", type=xbmcgui.INPUT_ALPHANUM)
		url = SEARCH_QUERY + urllib.quote_plus(search_string)
		data_set = link_getter(url=url, page=page)
		for data_single in data_set:
			title = data_single["title"]
			link = data_single["link"]
			since_time = data_single["since_time"]
			since_num_only = data_single["since_num_only"]
			main_list(name=title, link=link, since_time=since_time, back_url=URL_hin, action="play", isFolder=False)
	# elif flag == "play":
	# 	xbmc.log(">> flag play", 2)
	# 	# play_link = get_playable_link(s_link)
	# 	if play_link.endswith(".mp4"):
	# 		xbmc.Player().play(play_link)


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
		if "action" in param:
			if param["action"] == "new_list":
				if not "nextPageToken" in param or param["nextPageToken"] < 1:
					show_list(flag="new_list")
				elif "nextPageToken" in param and param["nextPageToken"] > 1:
					show_list(flag=param["action"], page=param["nextPageToken"])
				else:
					xbmcgui.Dialog().ok("SrHin", "You are at end of this page")
			elif param["action"] == "popular_list":
				show_list(flag="popular_list")
			elif param["action"] == "play":
				xbmc.log("> In param link : playing......" + str(param["link"]), 2)
				path = urllib.unquote_plus(param["link"])
				# xbmcgui.Dialog().ok("URL", path)
				r = requests.head(path, allow_redirects=True)
				# xbmc.log("in try with response.....: {}".format(r), 2)
				path = r.url
				xbmc.log("in try with new url......: {}".format(path), 2)
				# path = param["link"]
				# play_item = xbmcgui.ListItem(path=path)
				# xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
				# xbmc.executebuiltin("PlayMedia(param['link'])")
				xbmc.log("playing the path/url::::: {}".format(path), 2)
				xbmc.Player().play(path)
			elif param["action"] == "search":
				show_list(flag="search")
		else:
			xbmc.log("> In param : listing", 2)
			show_list(param["link"], param["nextPageToken"])
	else:
		xbmc.log("> In param else", 2)
		show_list(flag="main")


if __name__ == "__main__":
	xbmc.executebuiltin('UpdateAddonRepos()')
	xbmc.sleep(200)
	xbmc.executebuiltin('UpdateLocalAddons()')
	main()
	# data_set = link_getter(NEW_VID_URL_hin)
	xbmcplugin.endOfDirectory(_handle,  cacheToDisc=False)
