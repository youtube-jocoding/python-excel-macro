import pyautogui
import pyperclip
import time
import sys
import pandas as pd

df = pd.read_excel('feeling.xlsx', sheet_name='Sheet1')
words = df[df["감정범주"].isin(["기쁨","흥미"])].sort_values(by='감정정도M', ascending=False)[:50][["단어"]].drop_duplicates().values.flatten()

def click(x,y):
    time.sleep(0.5)
    pyautogui.moveTo(x,y)
    pyautogui.click(clicks=1)
    time.sleep(0.5)

for i in range(len(words)):
    click(482,998)
    click(630,568)
    pyperclip.copy(words[i])
    pyautogui.hotkey("ctrl", "v")
    click(1124,731)