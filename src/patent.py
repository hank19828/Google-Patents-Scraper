
import requests as rq
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
options=Options()
browser=webdriver.Chrome()
url="https://patents.google.com/patent/US10127816B2/en"
browser.get(url)
patent_number=browser.find_element(By.XPATH, "/html/body/search-app/search-result/search-ui/div/div/div/div/div/result-container/patent-result/div/div/div/div[1]/div[2]/section/header/h2").text
abstract=browser.find_element(By.XPATH, "/html/body/search-app/search-result/search-ui/div/div/div/div/div/result-container/patent-result/div/div/div/div[1]/div[1]/section[1]/patent-text/div/section/abstract/div").text
classification=browser.find_element(By.XPATH, "/html/body/search-app/search-result/search-ui/div/div/div/div/div/result-container/patent-result/div/div/div/div[1]/div[1]/section[3]/classification-viewer/div/classification-tree/div/div/div/div[6]/concept-mention/span/state-modifier/a").text
print(patent_number)
print(classification)
browser.close()
