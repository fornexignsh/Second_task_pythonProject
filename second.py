from selenium import webdriver
from selenium.webdriver.common.by import By
import os

chrome_driver_path = "C:\\chromedriver\\chromedriver.exe"

os.environ["PATH"] += os.pathsep + chrome_driver_path

driver = webdriver.Chrome()

driver.get("https://nexign.com/ru")

page_content = driver.find_element(By.TAG_NAME, "body").text

word_count = page_content.lower().count("nord")

print("Количество упоминаний слова 'Nord' на странице:", word_count)

driver.quit()
