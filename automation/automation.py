from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()

# Specify the path to the ChromeDriver
service = Service()

# Initialize the Chrome browser with options
chrome_browser = webdriver.Chrome(service=service, options=chrome_options)


chrome_browser.get('https://www.google.com')

assert 'Google' in chrome_browser.title

button = chrome_browser.find_element(
    By.CLASS_NAME, 'RNmpXc').get_attribute('value')

print(button)

# This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()


# user_message = chrome_browser.find_element(By.ID, 'user-message')
# user_message.clear()
# user_message.send_keys('I AM EXTRA COOOOL')

# time.sleep(2)
# show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# show_message_button.click()

# output_message = chrome_browser.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOL' in output_message.text


# Prevent the browser from closing immediately
input("Press Enter to close the browser...")

# Close the browser after input
chrome_browser.quit()
