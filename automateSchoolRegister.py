from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "PATH/TO/CHROMEDRIVER"
SITE = "URL"
EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
NAME = "NAME"
FORM = "FORM CLASS"

# Configure headless chrome
options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(PATH, options=options)
wait = WebDriverWait(driver, 10)

# Open site and enter email
driver.get(SITE)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys(EMAIL, Keys.RETURN)

# Enter password
input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
wait.until(EC.visibility_of(input))
input.send_keys(PASSWORD, Keys.RETURN)

# Input Google form details
wait.until(EC.title_is("6th Form Register"))
input = driver.find_element(By.XPATH, "//input[@type='text']")
input.send_keys(NAME, Keys.TAB, FORM, Keys.TAB, Keys.RETURN)

wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your response has been recorded')]")))
driver.quit()
