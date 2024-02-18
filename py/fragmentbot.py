from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip

#Menu
vless = "/html/body/div[2]/div/div[6]/select[1]/option[1]"
vmess = "/html/body/div[2]/div/div[6]/select[1]/option[2]"
trojan = "/html/body/div[2]/div/div[6]/select[1]/option[3]"
option = input("Enter your Protocol : ")
if option == "1" :
    option2 = vless
if option == "2" :
    option2 = vmess
if option == "3" :
    option2 = trojan
uuid = input("Enter ypur UUID : ")

# Start a new instance of Chrome web browser
driver = webdriver.Chrome()

# Open the website
driver.get("https://wikm.ir/frag/")

# Find and click the option that reveals additional options
protocol = driver.find_element(By.ID,"protocol")
protocol.click()

# Wait , find and click on option
wait = WebDriverWait(driver, 10)
specific_option = driver.find_element(By.XPATH,option2)
specific_option.click()

# Find the input field using its ID 
input_field = driver.find_element(By.ID,"uuid")

# Type text into the input field
input_field.clear()
input_field.send_keys(uuid)

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
