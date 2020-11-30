
import pandas as pd 
from datetime import datetime
from selenium import webdriver
import time

PATH = "enteryourpathhere"
driver = webdriver.Chrome(PATH)

def openr(URL):
	driver.get(URL)

sched = pd.read_csv('monday.csv')
while True:
	now = datetime.now().strftime("%H:%M")
	if now in str(sched["timings"]):
		row = sched.loc[sched["timings"]==now]
		URL = str(row.iloc[0,1])
		openr(URL)
		time.sleep(50)
		print("Opened Zoom link")
