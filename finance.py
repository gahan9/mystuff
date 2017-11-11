import requests
from bs4 import BeautifulSoup
import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler as scheduler


URL = "https://finance.google.com/finance?q=NSE:"
NIFTY_URL = URL + "NIFTY"

def get_data(url=NIFTY_URL):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response

def parse_data(data, **kwargs):
    if kwargs:
        tag_name = kwargs["tag_name"]
        tag_class = kwargs["tag_class"]
        tag_id = kwargs["tag_id"]
    soup = BeautifulSoup(data.text, "html.parser")
    return soup.find(tag_name, {"id": tag_id})


def fin():
    print("{} - {}".format(datetime.datetime.now().ctime(), BeautifulSoup(get_data().text, "html.parser").find('span', {'id':'ref_207437_l'}).text))


def func():
    ls_TECHM = []
    while True:
        x = BeautifulSoup(get_data(URL+"TECHM").text, "html.parser").find('span', {'id':'ref_5955635_l'}).text
        print(x)
        ls_TECHM.append(float(x))


if __name__ == "__main__":
    response_data = get_data(NIFTY_URL)
    bs_data = parse_data(response_data, tag_name="span", tag_id="ref_207437_l", tag_class="fjfe-recentquotes-table")
    # sched = scheduler()
    # print("{} - {}".format(datetime.datetime.now().ctime(), bs_data.text))
    # sched.add_job(fin, 'interval', seconds=1)
    func()
    # sched.start()
