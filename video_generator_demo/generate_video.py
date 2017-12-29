#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import glob


def print_log(*args):
    for arg in args:
        try:
            import xbmc
            xbmc.log("{}".format(arg), 2)
        except ImportError:
            print(arg)


class FileNotFoundError(Exception):
    """Raised when the file does not exists"""
    def __init__(self, *args, **kwargs):
        print_log("File not exists : {0}".format(args))
        Exception.__init__(self, *args, **kwargs)


class VideoMaker(object):
    def __init__(self, *args, **kwargs):
        print_log("{:^25}".format("__INITIALIZED__"))
        self.supported_extension = ['jpg', 'jpeg', 'png']
        self.codec = kwargs['codec'] if 'codec' in kwargs else "mp4v"
        self.fps = kwargs['fps'] if 'fps' in kwargs else 5
        self.is_color = kwargs['is_color'] if 'is_color' in kwargs else True
        self.duration = 5
        self.width = '1920'
        self.height = '1080'

    def make_video(self, content, source_path=None, target_path=None, duration=5):
        import cv2
        four_cc = cv2.VideoWriter_fourcc(*self.codec)
        out_vid = content.split(".")[0] + ".mp4"
        image_file = os.path.join(source_path, content)
        img = cv2.imread(image_file)
        height, width, channels = img.shape
        size = img.shape[1], img.shape[0]
        target_path = os.path.join(target_path, out_vid)
        vid = cv2.VideoWriter(target_path, four_cc, self.fps, (width, height), self.is_color)
        x = 0
        while True:
            if not os.path.exists(image_file):
                raise FileNotFoundError(image_file)
            if size[0] != img.shape[1] and size[1] != img.shape[0]:
                img = cv2.resize(img, size)
            vid.write(img)
            x += 1
            if x > duration * self.fps:
                break
        vid.release()
        cv2.destroyAllWindows()
        return vid

    def execute(self, path=None, duration=5, target_path=None):
        contents = os.listdir(path)
        target_path = target_path if target_path else os.path.join(path, ".cache")
        if not os.path.exists(target_path):
            try:
                os.mkdir(target_path)
            except Exception as e:
                print_log(e)
                os.makedirs(target_path)
        if contents:
            for content in contents:
                content_extension = content.split(".")[-1]
                if content_extension in self.supported_extension:
                    self.make_video_ffmpeg(content, source_path=path, target_path=target_path, duration=duration)
                    print("Process for {} completed".format(content))
            return {"status": "Processing completed", "target_path": target_path}

    def make_video_ffmpeg(self, content, source_path=None, target_path=None, **kwargs):
        try:
            from ffmpy import ffmpy  # placed module in local
        except ImportError:
            raise FileNotFoundError("Dependency of ffmpeg broke!!!")
        duration = kwargs['duration'] if 'duration' in kwargs else self.duration
        input_image = os.path.join(source_path, content)  # set path for input location
        output_video_name = content.split('.')[-2] + ".mp4"  # name the output video
        output_video = os.path.join(target_path, output_video_name)  # set path for output location
        if os.path.exists(output_video):
            os.remove(output_video)  # remove existing video to avoid any overwrite exception
        # setup scale for video set to default values if no argument passed
        scale = "{}:{}".format(kwargs['w'], kwargs['h']) if 'w' in kwargs and 'h' in kwargs\
            else "{}:{}".format(self.width, self.height)
        # set output setting flags like duration encoding etc.
        output_settings = "-c:v libx264 -t {} -pix_fmt yuv420p -vf scale={}".format(duration, scale)
        ff = ffmpy.FFmpeg(
            inputs={input_image: '-loop 1'},  # loop to iterate same image again and again
            outputs={output_video: output_settings}
        )
        ff.run()


if __name__ == "__main__":
    WORKING_DIR = os.getcwd()
    glob.glob(WORKING_DIR)
    odd_path = os.path.join(WORKING_DIR, 'target1')
    even_path = os.path.join(WORKING_DIR, 'target2')
    paths = [odd_path, even_path]
    obj = VideoMaker()
    for location in paths:
        print(obj.execute(path=location, duration=5))

