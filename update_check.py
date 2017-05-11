"""
__author__ = 'gahan@quixom.com'
"""
from __future__ import print_function
# from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib2
import re
import time
import json

BASE_URL = 'https://www.tvaddons.ag/kodi-addons/'

FETCH_URL = 'https://www.tvaddons.ag/kodi-addons/show/'


def OpenPage(url):
    """
    
    :param url: e.g. 'https://www.tvaddons.ag/kodi-addons/'
    :return: bs4.BeautifulSoup
    """
    load_page = urllib2.urlopen(url)  # open url
    content = load_page.read()  # store page source in string format
    load_page.close()

    soup = BeautifulSoup(content, "html.parser")  # parse page as html-->type-'bs4.BeautifulSoup'
    return soup


def LoadTag(source, tag_name, tag_id=None):
    """
    :param source: bs4.BeautifulSoup
    :param tag_name: html tag
    :param tag_id: corresponding tag id
    :return: bs4.element.ResultSet
    """
    tag_part = source.findAll(tag_name, {'id': tag_id})  # goes to "<tag_name class="" id="tag_id">"
    return tag_part


def LoadUrlList(source, tag_name, tag_id=None):
    """ 
    :param source: bs4.element.Tag
    :param tag_name: html tag
    :param tag_id: corresponding tag id
    :return: list
    """
    url_source = []
    for item in source.findAll(tag_name):
        url_source.append(str(item[tag_id]))
    return url_source


def main(base_url):
    main_page = OpenPage(base_url)  # <class 'bs4.BeautifulSoup'>
    sub_page1 = LoadTag(main_page, 'ul', 'addonCategories')[0]  # <class 'bs4.element.Tag'>
    item_list = []
    main_dict = {'kind': 'kodi_plugin', 'source': base_url}
    category_dict = {}
    for category in sub_page1.findAll('li'):
        category_name = LoadUrlList(category, 'img', 'alt')
        category_url = LoadUrlList(category, 'a', 'href')
        if len(category_name) == len(category_url) == 1:
            category_name = category_name[0]  # <type 'str'>
            category_url = category_url[0]  # <type 'str'>
        else:
            pass
        category_dict[str(category_name)] = str(category_url)
    for categories in category_dict:
        print('working.', end='')
        categories_name = categories
        categories_url = category_dict[categories]

        internal_page = OpenPage(categories_url)  # <class 'bs4.BeautifulSoup'>
        sub_page2 = LoadTag(internal_page, 'ul', 'addonList')  # <class 'bs4.element.ResultSet'>
        for items in sub_page2:
            print('.', end='')
            for plugins in items.findAll('li'):
                plugin_dictionary = {'kind': categories_name, 'url': categories_url}
                print('.', end='')
                plugin_name = LoadUrlList(plugins, 'img', 'alt')  # <type 'list'>
                plugin_url = LoadUrlList(plugins, 'a', 'href')  # <type 'list'>
                if len(plugin_name) == len(plugin_url) == 1:
                    plugin_name = plugin_name[0]  # <type 'str'>
                    plugin_url = plugin_url[0]  # <type 'str'>
                else:
                    pass
                plugin_page = OpenPage(plugin_url)
                plugin_detail = LoadTag(plugin_page, 'div', 'addonDetail')[0]  # <class 'bs4.element.Tag'>
                plugin_meta_detail = LoadTag(plugin_detail, 'div', 'addonMetaData')[0]  # <class 'bs4.element.Tag'>
                try:
                    version = re.search('Version: (.+?)Released', plugin_meta_detail.text).group(1)
                except:
                    version = ''
                try:
                    released = re.search('Released: (.+?)Summary', plugin_meta_detail.text).group(1)
                except:
                    released = ''
                try:
                    summary = re.search('Summary: (.+?)Host', plugin_meta_detail.text).group(1)
                except:
                    summary = ''
                try:
                    download_link = plugin_meta_detail.find(href=re.compile("\.zip$"))['href']
                except:
                    download_link = ''
                # description = re.search('Kodi Addon Description:(.+?)Kodi Addon Dependencies', plugin_detail.text).group(1)
                # dependencies = re.search('Kodi Addon Dependencies:(.+?)Kodi Addon Changelog', plugin_detail.text).group(1)
                plugin_dictionary['plugin_name'] = str(plugin_name)
                plugin_dictionary['plugin_url'] = str(plugin_url)
                plugin_dictionary['version'] = str(version)
                plugin_dictionary['released'] = str(released)
                plugin_dictionary['summary'] = str(summary)
                plugin_dictionary['download_link'] = str(download_link)
                # plugin_dictionary['description'] = description
                item_list.append(plugin_dictionary)
        main_dict['items'] = item_list
        print()
    with open('video_plugin.json', 'w') as fp:
        json.dump(main_dict, fp, sort_keys=False, indent=4)
    # file_output = open('plugin_dictionary.txt', 'w')
    # file_output.write(str(main_dict))
    # file_output.close()


if __name__ == '__main__':
    start_time = time.clock()
    main(BASE_URL)
    print(time.clock() - start_time, "seconds")
