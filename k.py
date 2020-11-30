from time import time
import pandas as pd
from datetime import datetime
import pyautogui
import time
sched = pd.read_csv('monday.csv')
while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(sched["timings"]):
        time.sleep(60)
        openzoombtn = pyautogui.locateCenterOnScreen('openzoom.png')
        print(openzoombtn)
        pyautogui.moveTo(openzoombtn)
        pyautogui.click()
        print("Clicked the button")