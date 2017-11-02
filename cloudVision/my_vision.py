import os
import requests
import json
import generatejson
# import web_detect
from credential import API_K
# set up credential
os.popen("export GOOGLE_APPLICATION_CREDENTIALS='/home/quixom/get-time-2a50ffd022a2.json'")

L = ['vision.txt', 'vision.json']


class VisionUsage(object):
    def __init__(self, *args, **kwargs):
        self.file_name = os.path.basename(__file__)  # /home/quixom/mystuff/cloudVision/my_vision.py
        self.file_location = __file__.replace(os.path.basename(__file__), "")  # /home/quixom/mystuff/cloudVision/
        self.image_location = kwargs["image"]
        print(self.file_location, self.image_location)

    def image_data_generator(self, image_location, image_input_data="vision.txt", output_json="vision.json", **choices):
        choice = choices['detection_set']
        s = ""
        for k,v in choice.items():
            s += "{}:{} ".format(k,v)
        choice_set = s.strip()
        for fl in L:
            if os.path.exists(fl):
                os.remove(fl)
        with open(image_input_data, "w") as file_writer:
            contnet = "{} {}".format(image_location, choice_set)
            file_writer.write(contnet)
        stat = os.popen("python generatejson.py -i {} -o {}".format(image_input_data, output_json))


def data_fetcher(image_json_data, final_result_path):
    data = open('vision.json', 'rb').read()
    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key={}'.format(API_K),
                            data=data,
                            headers={'Content-Type': 'application/json'})
    with open(final_result_path, 'w') as writer:
        writer.write(response.text)


def web_detector(image_uri):
    stat = os.popen("python web_detect.py {}".format(image_uri))
    with open("web_detect_{}.txt".format(image_uri), "w") as f:
        f.write(stat.read())

if __name__ == "__main__":
    detection_set = {0:10, 1:10, 2:10, 3:10, 4:10, 5:10, 6:10}
    image_detection_obj = VisionUsage(image="/home/quixom/mystuff/cloudVision/demo2.png")
    # pprint(dir(__file__))
    # image_data_generator(image_location='Honda_Accord.png',
                        # image_input_data=L[0], output_json=L[1], detection_set=detection_set)
    # data_fetcher(image_json_data=L[1], final_result_path="detail.json")
