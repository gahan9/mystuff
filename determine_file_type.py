"""
Determine File type by extension
"""

import os


class DetermineFile(object):
    video_extension = ['.mp4', '.mkv', '.avi', '.flv', '.vob', '.swf', '.mov', '.wmv', '.3gp']
    image_extension = ['.jpg', '.png', '.bmp', '.gif', '.jpeg', '.svg', '.ico']
    archive_extension = ['.zip', '.rar', '.gz', '.gz', '.7z', '.gzip', '.tar']
    document_extension = ['.txt', '.doc']

    def __init__(self, file=None):
        self.file_name, self.ext = os.path.splitext(file)  # file name or location with extension

    @property
    def is_video(self):
        if self.ext in self.video_extension:
            return True

    @property
    def is_image(self):
        if self.ext in self.image_extension:
            return True

    @property
    def is_archive(self):
        if self.ext in self.archive_extension:
            return True

    @property
    def is_document(self):
        if self.ext in self.document_extension:
            return True

    @property
    def file_type(self):
        if not self.ext:
            _type = "No extension"
        elif self.is_image:
            _type = "Image"
        elif self.is_video:
            _type = "Video"
        elif self.is_archive:
            _type = "Archive"
        elif self.is_document:
            _type = "Document"
        else:
            _type = "Other"
        _ext = '({})'.format(self.ext) if self.ext else ''
        return '\t{} - {}'.format(self.file_name, _type) + _ext

    def get_file_type(self, file=None):
        self.file_name, self.ext = os.path.splitext(file)
        print("source: {}".format(file))
        return self.file_type


if __name__ == "__main__":
    obj = DetermineFile('/home/user/Downloads/a.tar')
    print(obj.file_type)
    print(obj.get_file_type('a'))
    print(obj.get_file_type('a image.png'))
    print(obj.get_file_type('demo.jpeg'))
    print(obj.get_file_type('demovid.mp4'))
    print(obj.get_file_type('demovid.mkv'))
    print(obj.get_file_type('/home/user/Downloads/a.gzip'))
