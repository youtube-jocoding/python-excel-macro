import pyautogui as pg
import time

for i in range(30):
    print(pg.position())
    time.sleep(0.3)