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

    def make_video(self, content, source_path=None, target_path=None, format="mp4v", fps=5, is_color=True):
        four_cc = cv2.VideoWriter_fourcc(*format)
        out_vid = content.split(".")[0] + ".mp4"
        image_file = os.path.join(source_path, content)
        img = cv2.imread(image_file)
        height, width, channels = img.shape
        size = img.shape[1], img.shape[0]
        target_path = os.path.join(target_path, out_vid)
        vid = cv2.VideoWriter(target_path, four_cc, fps, (width, height), is_color)
        x = 0
        while True:
            if not os.path.exists(image_file):
                raise FileNotFoundError(image_file)
            if size[0] != img.shape[1] and size[1] != img.shape[0]:
                img = cv2.resize(img, size)
            vid.write(img)
            x += 1
            if x > fps*fps:
                break
        vid.release()
        cv2.destroyAllWindows()
        return vid

    def execute(self, path=None):
        contents = os.listdir(path)
        target_path = os.path.join(path, ".cache")
        if not os.path.exists(target_path):
            os.mkdir(target_path)
        if contents:
            for content in contents:
                content_extension = content.split(".")[-1]
                if content_extension in self.supported_extension:
                    self.make_video(content, source_path=path, target_path=target_path)
            return "Processing completed"


if __name__ == "__main__":
    working_dir = os.getcwd()
    odd_path = os.path.join(working_dir, 'target1')
    even_path = os.path.join(working_dir, 'target2')
    paths = [odd_path, even_path]
    obj = VideoMaker()
    for path in paths:
        print(obj.execute(path=path))

