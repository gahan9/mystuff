#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import cv2


def print_log(*args):
    for arg in args:
        try:
            import xbmc
            xbmc.log("{}".format(arg), 2)
        except Exception as e:
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

    def make_video(self, content, source_path=None, target_path=None, duration=5):
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
                    self.make_video(content, source_path=path, target_path=target_path, duration=duration)
                    print("Process for {} completed".format(content))
            return {"status": "Processing completed", "target_path": target_path}


if __name__ == "__main__":
    working_dir = os.getcwd()
    odd_path = os.path.join(working_dir, 'target1')
    even_path = os.path.join(working_dir, 'target2')
    paths = [odd_path, even_path]
    obj = VideoMaker()
    for location in paths:
        print(obj.execute(path=location, duration=50))

