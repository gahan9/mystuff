#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import ntpath
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
def print_log(*args):
    for arg in args:
        try:
            import xbmc
            xbmc.log("{}".format(arg), 2)
        except:
            print(arg)

class FileNotFoundError(Exception):
    """Raised when the file does not exists"""
    def __init__(self,*args,**kwargs):
        print_log("File not exists : {0}".format(args))
        Exception.__init__(self,*args,**kwargs)


class VideoMaker(object):
    def __init__(self,*args,**kwargs):
        print_log("{:^25}".format("__INITIALIZED__"))
        self.supported_extension = ['jpg', 'jpeg', 'png']

    def make_video(self, content, source_path=None, target_path=None, outimg=None, fps=5, size=None, is_color=True, format="mp4v"):
        fourcc = cv2.VideoWriter_fourcc(*format)
        vid = None
        outvid = content.split(".")[0] + ".mp4"
        x = 0
        while True:
            image_file = os.path.join(source_path, content)
            if not (image_file.endswith(".png") or image_file.endswith(".jpg")):
                print_log("Invalid file")
                break
            print_log("image_file path: " + str(image_file))
            if not os.path.exists(image_file):
                raise FileNotFoundError(image_file)
                break
            img = imread(image_file)
            frame = cv2.imread(image_file)
            height, width, channels = frame.shape
            if vid is None:
                if size is None:
                    size = img.shape[1], img.shape[0]
                vid = VideoWriter(os.path.join(target_path, outvid), fourcc, 1, (width, height), is_color)
            if size[0] != img.shape[1] and size[1] != img.shape[0]:
                img = resize(img, size)
            vid.write(img)
            x = x + 1
            if int(x) == int(fps):
                break
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
                    print_log(content)
                    self.make_video(content, source_path=path, target_path=target_path)

def main():
    odd_path = os.path.join(os.getcwd(), 'target1')
    even_path = os.path.join(os.getcwd(), 'target2')
    paths = [odd_path, even_path]
    for path in paths:
        obj = VideoMaker().execute(path=path)

main()