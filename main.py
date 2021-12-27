import pyautogui as pgui
import time
from tesserocr import PyTessBaseAPI, PSM
import os
image_file = '/home/rody/Pictures/sushida/sushida.png'
dir_path = '/home/rody/Pictures/sushida'

time.sleep(1)
pgui.press('enter')
time.sleep(2)
while True:
    os.mkdir(dir_path)
    #sc = pgui.screenshot(region=(300,492,340,31))
    sc = pgui.screenshot(region=(323,491,305,25))
    sc.save(image_file)
    api = PyTessBaseAPI(psm = PSM.AUTO, lang = 'eng')
    api.SetImageFile('/home/rody/Pictures/sushida/sushida.png')
    pgui.typewrite(api.GetUTF8Text())
    print(api.GetUTF8Text())
    moji = str(api.GetUTF8Text())
    os.remove(image_file)
    os.rmdir(dir_path)
    if len(moji) == 0:
        break