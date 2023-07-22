# -*- coding: utf-8 -*-
"""

@author: IdrisIbrahimERTEN
"""

import os
import shutil

ses = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
       ".alac", ".amr", ".ape", ".au", ".dss",
       ".flac", ".flv", ".m4a", ".m4b", ".m4p",
       ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
       ".opus", ".qcp", ".tta", ".voc", ".wav",
       ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

resim = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
         ".gif", ".webp", ".svg", ".apng", ".avif")

def is_audio(file):
    return os.path.splitext(file)[1].lower() in ses

def is_video(file):
    return os.path.splitext(file)[1].lower() in video

def is_image(file):
    return os.path.splitext(file)[1].lower() in resim

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext.lower() in resim) and "screenshot" in name.lower()

source_dir = "kaynak dosya yolu"
destination_dir = "hedef dosya yolu"

os.chdir(source_dir)

for file in os.listdir():
    if is_audio(file):
        shutil.move(file, os.path.join(destination_dir, "ses"))
    elif is_video(file):
        shutil.move(file, os.path.join(destination_dir, "video"))
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, os.path.join(destination_dir, "ekranfoto"))
        else:
            shutil.move(file, os.path.join(destination_dir, "resim"))
    else:
        shutil.move(file, os.path.join(destination_dir, "result"))
