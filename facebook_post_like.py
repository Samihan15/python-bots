from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usn = "samihannandedkar@gmail.com"
pas = "######"
txt = "Hello world"

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com/login/")
driver.maximize_window()

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginbutton")))

username.send_keys(usn)
password.send_keys(pas)
login_btn.click()

time.sleep(5)

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
except Exception as e:
    pass

post = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"What\'s on your mind, Samihan?")]'))
)

driver.execute_script("arguments[0].scrollIntoView(true);", post)
time.sleep(1)
driver.execute_script("arguments[0].click();", post)

post_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]')))
post_text.send_keys(txt)

# Correct the post_btn locator (use a tuple)
post_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Post')]")))
post_btn.click()

time.sleep(10)
driver.quit()
