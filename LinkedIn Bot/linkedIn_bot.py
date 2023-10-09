from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

def main():
    url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin" # url of LinkedIn
    network_url = "https://www.linkedin.com/mynetwork/" # url of LinkedIn network page
    driver = webdriver.Chrome(options=options) 
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
    start_bot(driver, url, network_url)

def login_to_linkedin(driver):
    username = driver.find_element(By.ID, "username")
    # you can also take username and password from user aswell here using python.
    username.send_keys("Your Email or Phone")
    password = driver.find_element(By.ID, "password")
    password.send_keys("Your Passowrd")
    try:
        driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large").click()
    except Exception as e:
        print(e) 

def  goto_network_page(driver,network_url):
    driver.get(network_url)

def  accept_invitations_from_users(driver):    
    # Scroll to the top of the page
    driver.execute_script("window.scrollTo(0, 0)")
    
    element_exists =  True
    # flag=1 # to accept only the first invitation
    while element_exists: # and flag
        try:
            # Find the invitation element
            driver.find_element(By.CSS_SELECTOR, '.invitation-card__action-container.pl3')
        except NoSuchElementException as e:  # handle the element not existing
            element_exists =  False
            print(e)
        finally:
            if element_exists:
                driver.find_element(By.CSS_SELECTOR, "button.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.invitation-card__action-btn").click()
                # flag -= 1

def  start_bot(driver,url,network_url):
    driver.get(url)
    login_to_linkedin(driver)
    goto_network_page(driver,network_url)
    accept_invitations_from_users(driver)

# Driver's code
if __name__ == "__main__":
    main()