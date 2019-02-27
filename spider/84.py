from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
wait=WebDriverWait(browser,100)
#input=wait.until(EC.presence_of_element_located((By.ID,'q')))
#print(input)
button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.search-bd .search-panel .search-button .btn-search')))
print(button)