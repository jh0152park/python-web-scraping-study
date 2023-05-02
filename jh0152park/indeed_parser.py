from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://kr.indeed.com/jobs?q="
TERM = "python"

driver = webdriver.Chrome()
driver.get(URL)
print(driver.page_source)
