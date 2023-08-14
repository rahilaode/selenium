# load Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

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