from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()

driver.get("http://siakad.polinema.ac.id/")

username = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
username.click()
username.send_keys("********")
password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
password.click()
password.send_keys("********")
password.send_keys(Keys.ENTER)

# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")