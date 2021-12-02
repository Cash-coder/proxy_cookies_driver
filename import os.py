import os

path = 'cookies_folder'

obj = os.scandir(path)

for e in obj:
    print(e)