from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip

Text = input("Enter Your conf : ")
# Start a new instance of Chrome web browser
driver = webdriver.Chrome()

# Open the website
driver.get("https://ircfspace.github.io/fragment")

# Find the input field using its ID 
input_field = driver.find_element(By.ID,"defConfig")

# Type text into the input field
input_field.clear()
input_field.send_keys(Text)

# Find the button element by its ID 
check = driver.find_element(By.ID,"checkConf")

# Click the button
check.click()

# click on mux
mux = driver.find_element(By.XPATH,"//button[@data-i18n='config_switch_mux']")
mux.click()

# click and fill length
length = driver.find_element(By.ID,"length")
length.clear()
length.send_keys("10-20")

# click and fill interval
interval = driver.find_element(By.ID,"interval")
interval.clear()
interval.send_keys("10-20")

#done
done = driver.find_element(By.ID,"qrGen")
done.click()

#click on copy button
copy_button = driver.find_element(By.ID,"copyCode")
copy_button.click()

#copy from cipboard to var
copied_text = pyperclip.paste()
# Close the browser
driver.quit()
