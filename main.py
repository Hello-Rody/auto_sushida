import pyautogui as pgui
import time
from tesserocr import PyTessBaseAPI, PSM
import os
dir_path = '任意のディレクトリのパス'

time.sleep(1)
pgui.press('enter')
time.sleep(2)
while True:
    os.mkdir(dir_path+"sushdia/")
    sc = pgui.screenshot(region=(x,y,x,y))
    sc.save(dir_path+"sushida.png")
    api = PyTessBaseAPI(psm = PSM.AUTO, lang = 'eng')
    api.SetImageFile(dir_path+"sushida.png")
    pgui.typewrite(api.GetUTF8Text())
    print(api.GetUTF8Text())
    moji = str(api.GetUTF8Text())
    os.remove(dir_path+"sushida.png")
    os.rmdir(dir_path+"sushida/")
    if len(moji) == 0:
        break