#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import threading
import sys
import subprocess
import locale
import re
try:
    import xbmc
except ImportError:
    pass

try:
    ADDON_ID = 'screensaver.customslideshow'
    ADDON_PATH = xbmc.translatePath('special://home/addons/'+ADDON_ID)
    if not os.path.exists(ADDON_PATH):
        try:
            from service import ADDON_HOME
            from service import ADDON_ID
            ADDON_PATH = xbmc.translatePath('special://home/addons/' + ADDON_ID)
        except Exception as e:
            pass
except NameError:
    ADDON_PATH = os.getcwd()


def print_log(*args, debug=True):
    if debug:
        try:
            if 'ADDON_ID' not in globals() and 'ADDON_ID' not in locals():
                ADDON_ID = "CUSTOM_NOTICE>> "
            prefix = ADDON_ID
        except:
            prefix = "CUSTOM_NOTICE>> "
        for arg in args:
            try:
                import xbmc
                xbmc.log("{} :: {}".format(prefix, arg), 2)
            except ImportError:
                print("{} :: {}".format(prefix, arg))


def set_env(**kwargs):
    for key, value in kwargs.items():
        os.environ[key] = value


class FileNotFoundError(Exception):
    """Raised when the file does not exists"""

    def __init__(self, *args, **kwargs):
        print_log("File not exists : {0}".format(args))
        Exception.__init__(self, *args, **kwargs)


class VideoMaker(object):
    def __init__(self, *args, **kwargs):
        set_env(ffmpeg=ADDON_PATH)
        # print_log("{:^25}".format("__INITIALIZEDssss__"))
        self.supported_extension = ['jpg', 'jpeg', 'png']
        self.video_extension = ['mp4', 'mkv']
        self.codec = kwargs['codec'] if 'codec' in kwargs else "mp4v"
        self.fps = kwargs['fps'] if 'fps' in kwargs else 2
        self.duration = 5
        self.width = '1280'
        self.height = '720'
        self.fade_start = 0
        self.fade_duration = 1.5

    def execute(self, path=None, duration=5, target_path=None, multi_threading=False, **kwargs):
        contents = os.listdir(path)
        target_path = target_path if target_path else os.path.join(path, ".cache")
        if not os.path.exists(target_path):
            try:
                os.mkdir(target_path)
            except Exception as e:
                print_log(e)
                os.makedirs(target_path)
        if contents:
            if multi_threading:
                threading.Thread(target=self.convert_bulk, args=(contents, path, target_path, duration )).start()
            else:
                self.convert_bulk(contents, path, target_path, duration)
            return {"status": "Processing completed", "target_path": target_path}

    def convert_bulk(self, contents, path, target_path, duration):
        for content in contents:
            content_extension = content.split(".")[-1]
            if content_extension in self.supported_extension:
                self.make_video_ffmpeg(content, source_path=path, target_path=target_path, duration=duration)
                print("Process for {} completed".format(content))
            elif content_extension in self.video_extension:
                # by change if content is video
                pass
        # return {"status": "Processing completed", "target_path": self.target_path}

    def make_video_ffmpeg(self, content, source_path=None, target_path=None, flag="keep", **kwargs):
        """
        BASE_COMMAND C:\Users\Quixom\AppData\Roaming\Kodi\addons\screensaver.customslideshow\ffmpeg.exe -loop 1 -i C:\Users\Quixom\AppData\Roaming\Kodi\ScreenSaver_ADDON\even_anonymous\anonymous_1920x1200.jpg -c:v libx264 -t 5 -pix_fmt yuv420p -vf scale=1920:1080 C:\Users\Quixom\AppData\Roaming\Kodi\ScreenSaver_ADDON\even_anonymous\.cache\a.mp4
        BASE_COMMAND <ffmpeg-path> -loop 1 -i <image_path> -c:v libx264 -t <duration> -pix_fmt yuv420p -vf "fade=t=in:st=<fade-start-time>:d=<fade-duration>" -r <fps> -s <width>x<height> <target-video>
        example: ffmpeg -loop 1 -i 1.jpg -c:v libx264 -t 5 -pix_fmt yuv420p -vf "fade=t=in:st=0:d=1.5" -r 2 -s 1280x720 1.mp4
        :param content: full absolute image path
        :param source_path: image location
        :param target_path: store video at this location
        :param kwargs:
            duration: video duration
            h: height for video
            w: width for video
            fade_start: start time of fade
            fade_duration: duration of fade to stop
        :param flag: flag set to decide whether video need to generate for image or not
            flag='remove': to remove/overwrite file
        :return: generates video to target_path
        """
        try:
            from ffmpy import ffmpy  # placed module in local
        except ImportError:
            raise FileNotFoundError("Dependency of ffmpeg broke!!!")
        duration = kwargs.get('duration', self.duration)
        fade_start = kwargs.get('fade_duration', self.fade_start)
        fade_duration = kwargs.get('fade_duration', self.fade_duration)
        if fade_duration >= duration:
            fade_duration = duration / 5
        try:
            input_image = os.path.join(source_path, content)  # set path for input location
        # except UnicodeDecodeError:
        #     xbmc.log("Error for UnicodeEncodeError>>6 :", 2)
        #     return None
        except Exception as err:
            xbmc.log("GOT UnicodeEncodeError>>>mk>6 :", 2)
            return None
        output_video_name = content.split('.')[-2] + ".mp4"  # name the output video
        output_video = os.path.join(target_path, output_video_name)  # set path for output location
        # setup scale for video set to default values if no argument passed
        scale = "{}x{}".format(kwargs.get('w', self.width), kwargs.get('h', self.height))
        # set output setting flags like duration encoding etc.
        fade_setting = "fade=t=in:st={0}:d={1}".format(fade_start, fade_duration)
        output_settings = "-c:v libx264 -t {0} -pix_fmt yuv420p -vf {1} -s {2}".format(duration, fade_setting, scale)
        if sys.platform == 'win32':
            ff = ffmpy.FFmpeg(
                executable=os.path.join(ADDON_PATH, 'ffmpeg.exe'),
                inputs={input_image: '-loop 1'},  # loop to iterate same image again and again
                outputs={output_video: output_settings}
            )
        else:
            ff = ffmpy.FFmpeg(
                inputs={input_image: '-loop 1'},  # loop to iterate same image again and again
                outputs={output_video: output_settings}
            )
        """
        ff = ffmpy.FFmpeg(
            inputs={r"C:\Users\Quixom\AppData\Roaming\Kodi\ScreenSaver_ADDON\even_anonymous\0124654c7950f4f823c1092c60837ccc.jpg": '-loop 1'},
            outputs={r"C:\Users\Quixom\AppData\Roaming\Kodi\ScreenSaver_ADDON\even_anonymous\.cache\0124654c7950f4f823c1092c60837ccc.mp4": "-c:v libx264 -t 5 -pix_fmt yuv420p -vf scale=1920:1080"}
        )
        """
        # print_log(input_image, output_video, output_settings, ff.cmd)
        if os.path.exists(output_video):
            if flag == "remove":
                try:
                    os.remove(output_video)  # remove existing video to avoid any overwrite exception
                    os.popen(ff.cmd)
                except Exception as err:
                    xbmc.log("Error for WindowsError :>>8", 2)
                    pass
        else:
            try:
                os.popen(ff.cmd)
            except UnicodeDecodeError:
                xbmc.log("Error for UnicodeDecodeError>vm>6 :", 2)
                return None
            except UnicodeEncodeError:
                # subprocess.Popen(ff.cmd.encode(locale.getpreferredencoding()), shell=True)
                xbmc.log("Error for UnicodeEncodeError>vm>7", 2)
                return None

    def get_video_duration(self, video_file_path):
        print_log("IN get_video_duration :", str(video_file_path))
        if os.path.exists(video_file_path):
            try:
                if sys.platform == "win32":  # for windows
                    ffmpegs = os.path.join(ADDON_PATH, 'ffmpeg.exe')
                    process = subprocess.Popen([ffmpegs, '-i', video_file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    stdout, stderr = process.communicate()
                    matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()
                    # print matches['hours']
                    # print matches['minutes']
                    return matches['seconds']
                else:
                    result = subprocess.Popen(["ffprobe", video_file_path],  # for linux
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    video_details = [x for x in result.stdout.readlines() if "Duration" in x]
                    if video_details:
                        video_time = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", video_details[0], re.DOTALL).groupdict()
                        print_log("seconds :", video_time["seconds"])
                        return video_time["seconds"]
            except UnicodeDecodeError:
                xbmc.log("Error for UnicodeDecodeError>vm>6 :", 2)
                return None
            except UnicodeEncodeError:
                xbmc.log("GOT UnicodeEncodeError>>>> in videomaker :", 2)
                return None


def main(image_list):
    set_env(ffmpeg=ADDON_PATH)
    obj = VideoMaker()
    try:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        obj.execute(path=image_list)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
    except NameError:
        obj.execute(path=image_list)
