import os
import shutil
import send2trash

DownFolder = 'C:\\Users\\anmen\\Downloads'

def fileEx(DownFolder):
    for file in os.listdir(DownFolder):
        # script moves files with .jpeg or .png format to Wallpaper folder
        if file.endswith('.jpg') or file.endswith('.png'):
            shutil.move(DownFolder+'\\'+file, 'C:\\Users\\anmen\\Documents\\Wallpapers')
        # script moves .pdf format to Books folder
        elif file.endswith('.pdf'):
            shutil.move(DownFolder+'\\'+file, 'C:\\Users\\anmen\\Documents\\Study\\IT Books')
        # moves others to trash
        else:
            send2trash.send2trash(DownFolder+'\\'+file)

fileEx(DownFolder)