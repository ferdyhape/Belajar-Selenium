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

wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-action-wrapper"]/h3[2]/a')))
element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'page-title'), 'FERDY'))

driver.execute_script('''window.open("https://slc.polinema.ac.id/spada/","_blank");''')