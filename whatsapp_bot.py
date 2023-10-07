from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import schedule
from selenium.webdriver.support import expected_conditions as ec

time_hours = 23  # here the enter the hour at which you want to schedule the message (24 Hours format)
time_minutes = 7  # enter the minutes
to_person = 'Sarvesh Roomate'  # enter the name of the person you have to send the message from your contact list
message = "Hello, this is Sarvesh"  # enter message
schedule_once = True  # If you want to send the message everyday at that time make it False

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 100)  # Adjust the timeout as needed
driver.get("https://web.whatsapp.com")
print("Scan QR Code")
print("Logged In")


def send_whatsapp_message():
    print("Sending scheduled message...")
    contact_path = '//span[contains(@title, "' + to_person + '")]'
    try:
        contact = wait.until(ec.presence_of_element_located((By.XPATH, contact_path)))
        time.sleep(2)
        contact.click()
        time.sleep(2)
        message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        message_box = wait.until(ec.presence_of_element_located((By.XPATH, message_box_path)))
        message_box.send_keys(message + Keys.ENTER)
        time.sleep(2)
        print("Message sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


if time_minutes < 10:
    minu = "0" + str(time_minutes)
else:
    minu = str(time_minutes)
timer = str(time_hours) + ":" + minu
schedule.every().day.at(timer).do(send_whatsapp_message)
schedule.every().day.at(timer).do(send_whatsapp_message)
while True:
    if schedule_once:
        current_time = time.time()
        local_time = time.localtime(current_time)

        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        microsecond = int((current_time - int(current_time)) * 1000000)
        if hour == time_hours and minute == time_minutes:
            send_whatsapp_message()
            time.sleep(5)
            break

    else:
        schedule.run_pending()
        time.sleep(1)
