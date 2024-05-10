import pandas as pd

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

nome_arquivo = "pod_back.csv"

value = str
df = pd.read_csv(nome_arquivo)

for index, row in df.iterrows():
    print("index: " + str(index) + "POD" + row[0])   
    page.goto("https://sterling.quick.aero/tracking/")
    page.fill("input[class='form-control']")
    page.wait_for_timeout(5000)
    page.click("button[class='button button-long red-button']")
    page.wait_for_timeout(5000)
    print(page.title())
    browser.close()
 