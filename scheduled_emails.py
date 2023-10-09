import os
import time
from selenium import webdriver

email = os.envoron.get("EMAIL")
password = os.environ.get("EMAIL_PASSWORD")
recipient_email = "recipient@example.com"
email_subject = "Scheduled Email"
email_message = "This is a scheduled email sent using Selenium."

def send_email():
    driver = webdriver.Chrome()
    driver.get("https://mail.google.com")
    driver.find_element_by_id("identifierId").send_keys(email)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[text()='Compose']").click()
    driver.find_element_by_name("to").send_keys(recipient_email)
    driver.find_element_by_name("subjectbox").send_keys(email_subject)
    driver.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys(email_message)
    driver.find_element_by_xpath("//div[contains(text(),'Send')]").click()
    driver.quit()

scheduled_time = "10:00"
while True:
    current_time = time.strftime("%H:%M")
    if current_time == scheduled_time:
        send_email()
        break
    time.sleep(60)

