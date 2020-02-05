import os
import shutil


def copy_songs(source_path, dest_path):
    for root, dirs, files in os.walk(source_path):  # replace the . with your starting directory
        for file in files:
            path_file = os.path.join(root, file)
            shutil.copy2(path_file, dest_path)  # change you destination dir


copy_songs(r'C:\Users\Eyal-TLV\Documents\NoteBurner Spotify Music Converter\Beast Mode', r'C:\Users\Eyal-TLV\Desktop\tmp')