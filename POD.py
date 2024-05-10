import pyperclip
import time
import pyautogui
import pandas as pd
import pyperclip
import openpyxl
import selenium
import copy 

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import workbook

nome_arquivo = "pod_back.csv"

value = str
df = pd.read_csv(nome_arquivo)

for index, row in df.iterrows():
    print("index: " + str(index) + "POD" + row[0])
    browser = p.chromium.launch(headless=False)page = browser.new_page()
    page11.goto("https://sterling.quick.aero/tracking/")
   
    page11.get_by_placeholder("Tracking number").fill(row[0])
    with page11.expect_popup() as page12_info:
        page11.get_by_role("link", name="Search").click()
    page12 = page12_info.value

    # ---------------------
    context.close()
 




#pyautogui.press('tab')
#pyautogui.press('tab')                  
#pyautogui.press('tab')
#pyautogui.press('tab')
#pyautogui.press('tab')      

#pyautogui.write('200580294M')

#pyautogui.press('enter')

#time.sleep(3)


#with pyautogui.hold('ctrl'):
    #pyautogui.press('c')

#pyautogui.press('win')
#pyautogui.write('notepad')
#pyautogui.press('enter')


 





#input()










    







