import xbmc
import xbmcgui
import requests
from bs4 import BeautifulSoup

ADDON_ID = "plugin.video.srHin"
ADDON_URL = "plugin://" + ADDON_ID + "/"

URL_POOL = ["https://free-proxy-list.net/"]
# PROXY_POOL = []
DATA_SET = []
NEW_VID_URL_hin = "https://www.fifastop.com/newvideos.php"


def main_list(name, thumb=None, mode, back_url=None, nextPageToken=None, isFolder=False, link=None, total_videos=None):
    xbmc.log('IN FUN=main_list()......', 2)  # log : NOTICE
    # xbmc.log('name : ' + str(name), 2)  # log : NOTICE
    u = PLUGIN_URL
    u += "?name=" + urllib.quote_plus(str(name))
    if not thumb:
    	thumb = xbmc.translatePath("special://home/addons/{}/icon.png".format(ADDON_ID))
    u += "&thumb=" + urllib.quote_plus(str(thumb))
    u += "&action=" + str(mode)
    u += "&link=" + str(link)
    u += "&back_url=" + str(back_url)
    u += "&nextPageToken=" + str(nextPageToken)
    xbmc.log('url ..........................: ' + urllib.unquote_plus(str(u)), 2)  # log : NOTICE

    # liz = xbmcgui.ListItem(label=cust_label, iconImage="", thumbnailImage=urllib.unquote_plus(thumb))
    # liz.setInfo(type="video", infoLabels={"label": name, "title": name})
    liz.addContextMenuItems([('Refresh', 'Container.Refresh')])
    # liz.setArt({'poster': thumb})
    # xbmcplugin.addDirectoryItem(handle=abs(int(sys.argv[1])), url=u, listitem=liz, isFolder=True)
    xbmcplugin.addDirectoryItem(abs(int(sys.argv[1])), u, liz, isFolder)


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


def link_getter(url=NEW_VID_URL_hin):
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
	url = soup.find_all("link", {"rel":"video_src"})[0]["href"]
	if url.startswith("http://video.fifastop.com/"):
		url = url.replace("http://video.", "https://www.")
	return url


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


if __name__ == "__main__":
	main()
	# data_set = link_getter(NEW_VID_URL_hin)
	xbmcplugin.endOfDirectory(_handle,  cacheToDisc=False)
