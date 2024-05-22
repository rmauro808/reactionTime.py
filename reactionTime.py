from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()

options.add_experimental_option("detach", True)


# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Navigate to game website
driver.get("https://www.arealme.com/reaction-test/en/")
driver.maximize_window()

#find the start button and click
click_start = driver.find_element(By.ID,"start")
click_start.click()

#wait 1 second for screen to load before moving on
time.sleep(1)

#Click "Anywhere on the screen"
ac = ActionChains(driver)
ac.move_by_offset(150, 150).click().perform()

#setting the range to equal the amount of attempts we have in game. 
for i in range(5):
  #looping over and over waiting for the class name of the button to switch from red, to green and then click. 
    while True:
        try:
            # Try to find the green button
            green_button = driver.find_element(By.CLASS_NAME, 'tfny-circleGreen')
            # If found, break the loop
            green_button.click()
            break
        except:
            # If not found, continue the loop
            pass
