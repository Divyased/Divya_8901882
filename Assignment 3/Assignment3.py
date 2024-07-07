from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the LinkedIn homepage
driver.get("https://ca.linkedin.com/")
time.sleep(5)

# Finding the "Sign in" button and clicking it
sign_in_button = driver.find_element("xpath", "/html/body/nav/div/a[2]")
sign_in_button.click()
time.sleep(5)

# Entering login credentials
username_field = driver.find_element("id","username")
username_field.send_keys("divya.ed10@gmail.com")
time.sleep(2)
password_field = driver.find_element("id","password")
password_field.send_keys("abcdefgh@1234")
time.sleep(2)
password_field.send_keys(Keys.RETURN)
time.sleep(5)

# Navigating to the network page
network_link = driver.find_element("xpath", "/html/body/div[5]/header/div/nav/ul/li[2]/a/span")
network_link.click()
time.sleep(5)

# Sending a connection request to a user
search_bar = driver.find_element("xpath","/html/body/div[5]/header/div/div/div/div[1]/input")
search_bar.send_keys("divya sirling edward")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# Clicking on the "Connect" button in the user's profile
connect_button = driver.find_element("xpath","/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div/div/ul/li/div/div/div/div[2]/div[1]/div/button")
connect_button.click()
time.sleep(5)

add_note = driver.find_element("xpath","/html/body/div[3]/div/div/div[3]/button[2]")
add_note.click()
time.sleep(5)

# Closing the webdriver
driver.close()





