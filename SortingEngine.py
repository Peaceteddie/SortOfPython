import os
import sys
import shutil

dictionary = {
    "Archives": ["zip", "rar", "7z", "ace", "cab", "tar", "jar", "pak", "wad"],
    "Audio": ["mp3", "wma", "wav", "ogg", "mid", "flac", "acc"],
    "Documents": [
        "doc",
        "docx",
        "pdf",
        "xls",
        "txt",
        "ppt",
        "htm",
        "php",
        "xml",
        "rtf",
        "log",
        "cs",
        "gdoc",
        "gsheet",
        "gslides",
        "gjam"
    ],
    "Ebooks": ["mobi", "lit", "azw", "epub"],
    "ISO Images": ["iso", "img", "nrg"],
    "Pictures": [
        "jpg",
        "jpeg",
        "gif",
        "png",
        "ico",
        "bmp",
        "psd",
        "tif",
        "pcx",
        "tga",
        "dib",
        "webp",
    ],
    "Programs": ["apk", "exe", "msi", "bat", "pif", "cmd", "btm", "sh"],
    "Shortcuts": ["lnk"],
    "Torrents": ["torrent"],
    "Videos": [
        "rm",
        "mp4",
        "mpg",
        "mpeg",
        "flv",
        "3gp",
        "rmvb",
        "avi",
        "wmv",
        "mkv",
        "vob",
        "mov",
        "webm",
    ],
}

path = sys.argv[1]

try:
    os.chdir(path)
except:
    exit()

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    ext = ext[1:]

    if ext == "":
        continue

    for cat in dictionary:
        if ext in dictionary[cat]:
            destination = f"{path}/{cat}"
            if not os.path.exists(destination):
                os.makedirs(destination)
            if os.path.exists(destination + "/" + file):
                for i in range(1, len(os.listdir(destination)) + 1):
                    modpath = f"{destination}/{ name} ({i}).{ext}"
                    if not os.path.exists(modpath):
                        shutil.move(f"{path}/{file}", modpath)
                        break
            else:
                shutil.move(f"{path}/{file}", destination)
