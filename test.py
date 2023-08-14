# # load Driver
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

# Choose the web page
driver.get("https://www.google.com/")

# Access the search box element
search_box = driver.find_element(by = By.NAME, 
                                 value = "q")

# Input "Selenium Tutorials" in the search box
search_box.send_keys("Selenium Tutorials")

# Access the button "Google search" element
button = driver.find_element(by = By.NAME, 
                             value = "btnK")

# Click the button
button.click()

# Get the title
title = driver.title

# Print the title
print(title)

driver.quit()





















# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_eight_components():
#     driver = webdriver.Chrome()

#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     print(value)
#     assert value == "Received!"

#     driver.quit()
    
# test_eight_components()