"""
This is common utility file intent to keep utilities created in python to be kept overtime!!!
"""

import os



def duplicate_file_remover(path):
    """Remove the duplicate files from directory structure
    """
    for root, folders, files in os.walk(path):
        for folder in folders:
            duplicate_file_remover(os.path.join(root, folder))
        for file in files:
            f_only = os.path.splitext(file)
            f1 = os.path.join(root, file)
            f2 = os.path.join(root, file.replace(' - Copy', ''))  # for windows!!!
            # TODO: map the other possibly duplicate file names i.e. (1), (2)....etc
            if f_only[0].endswith(' - Copy') and os.path.getsize(f1) == os.path.getsize(f2):
                if open(f1, 'rb').read() == open(f2, 'rb').read():
                    os.remove(f1)


