# -*- coding: utf-8 -*-
# !/usr/bin/python
# !/usr/bin/env python
__author__ = 'gahan'

import os, sys
import re
import subprocess
from datetime import datetime
import time
import platform
import json
import string
import xbmc

# ADDONS = xbmc.translatePath('special://userdata/')
PRODUCT_NAME = "Kodi"
XBMC_HOME = xbmc.translatePath('special://home/')  # C:\Users\Quixom\AppData\Roaming\Kodi\
# XBMC_HOME = r"C:\Users\Quixom\AppData\Roaming\Kodi"
# ADDON_FOLDER = xbmc.translatePath('special://home/addons/')
LOG_PATH = xbmc.translatePath('special://logpath/')  #  C:\Users\Quixom\AppData\Roaming\Kodi\kodi.log
LOG_PATH = os.path.join(XBMC_HOME, "{}.log".format(PRODUCT_NAME.lower()))
SERVER_LOG_DIRECTORY = os.path.join(XBMC_HOME, "logs")


class Logger(object):
    """ Logger """
    def __init__(self, log_to_parse=LOG_PATH):
        super(Logger, self).__init__()
        self.log_path = log_to_parse
        self.system_info = self.get_sys_info()
        self.unique_id = self.get_uuid()
        self.last_log_detail = os.path.join(SERVER_LOG_DIRECTORY, "last_log_detail.log")
        self.log_start = self.session_start(self.log_path) + ".log"  # str(2017-09-16_﻿12-13-40_UTC+0530)  + ".log"
        self.custom_log = os.path.join(SERVER_LOG_DIRECTORY, self.log_start)
        print(str(self.custom_log))
        self.log_parser(self.log_path)



    def get_macs_android(self):
        mac = ""
        eth0 = '/sys/class/net/eth0/address'
        wlan0 = '/sys/class/net/wlan0/address'
        if os.path.exists(eth0):
            e = open(eth0).read().strip()
            mac = e.upper()
        if os.path.exists(wlan0):
            w = open(wlan0).read().strip()
            mac = w.upper()
        if len(mac) > 2:
            return mac
        else:
            uid = os.popen("getprop ro.serialno").read()
            return uid


    def get_uuid(self):
        """
        find Universally unique identifier of device
        :return: uuid(for windows and mac os) / mac address(for android)
        """
        if sys.platform == 'win32':
            uid = os.popen("wmic csproduct get UUID").read().strip().split("\n")[-1]
            return uid
        elif sys.platform == 'darwin':
            mac_uid = subprocess.check_output("ioreg -rd1 -c IOPlatformExpertDevice | grep -E '(UUID)'", shell=True).split('"')[-2]
            return mac_uid
        elif sys.platform == 'linux2' or 'android':
            a_mac = get_macs_android()
            return a_mac
        else:
            return "UNKNOWN SYSTEM"


    def get_sys_info(self):
        platform_uname = platform.uname()
        platform_dict = {"system": platform_uname[0], "node": platform_uname[1], "release": platform_uname[2], "version": platform_uname[3],
                         "machine": platform_uname[4], "processor": platform_uname[5]}
        data = json.dumps(platform_dict)
        return data


    def session_start(self, log_file):
        if not os.path.exists(SERVER_LOG_DIRECTORY):
            os.mkdir(SERVER_LOG_DIRECTORY)
        if not log_file:
            log_file = self.log_path
        with open(log_file, "r") as line_reader:
            f_line = line_reader.readline()
        time_stamp = re.search(r"([0-9:]+)", f_line).group(0)
        # date = datetime.now().strftime('%Y-%m-%d')
        # time_zone = time.strftime("%z", time.gmtime())
        # log_line = "{0}_{1}_UTC{2}".format(date, time_stamp, time_zone)
        log_line = time_stamp
        # with open(self.last_log_detail, "w") as this_session:
        #     this_session.write(log_line)
        log_stamp = re.sub(":", "-", log_line)
        return log_stamp


    def log_parser(self, file_path):
        if not file_path:
            file_path = self.log_path
        print("In log parser..")
        with open(file_path) as f:
            while True:
                line = f.readline()
                if line:
                    with open(self.custom_log, 'a') as log_writer:
                        if "NOTICE: Starting {}".format(PRODUCT_NAME) in line:
                            # log_writer.write("SYSTEM_INFO: {0}\n".format(self.system_info))
                            # log_writer.write("SYSTEM_UNIQUE_ID: {0}\n".format(self.unique_id))
                            details = "TimeZone: UTC{} and date: {}".format(time.strftime("%z", time.gmtime()), datetime.now().ctime())
                            log_writer.write(line[:line.index("NOTICE:")] + ": {} service started ({})\n".format(PRODUCT_NAME, details))
                        if "NOTICE: VideoPlayer: Opening:" in line:
                            log_writer.write(line.replace("NOTICE: VideoPlayer: Opening:", ": Streaming: \n"))
                        if "CVideoPlayer::OnExit()" in line:
                            log_writer.write(line[:line.index("NOTICE:")] + ": VideoPlayer Stopped\n")
                        if "NOTICE: stop all" in line:
                            log_writer.write(line[:line.index("NOTICE:")] + "{} Service closed\n".format(PRODUCT_NAME))
                            break


def main_thread():
    os.chdir(XBMC_HOME)
    # print(os.getcwd())
    if os.path.exists(LOG_PATH):
        logger_object = Logger(LOG_PATH)


if __name__ == "__main__":
    xbmc.log("IN LOGGER..........", 2)
    main_thread()
    # for line in loglines:
    #     print(line,)
