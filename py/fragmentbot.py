from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import pyperclip

#Menu
vless = "/html/body/div[2]/div/div[6]/select[1]/option[1]"
vmess = "/html/body/div[2]/div/div[6]/select[1]/option[2]"
trojan = "/html/body/div[2]/div/div[6]/select[1]/option[3]"
ws = "/html/body/div[2]/div/div[6]/select[2]/option[1]"
grpc = "/html/body/div[2]/div/div[6]/select[2]/option[2]"

option = input("Enter your Protocol (vless=l , vmess=m , trojan=t) : ")
if option == "l" :
    option = vless
if option == "m" :
    option = vmess
if option == "t" :
    option = trojan
transmit = input("Enter ws or grpc : ")
if transmit == ws : 
    transmit = ws
else : 
    transmit = grpc
uuid = input("Enter ypur UUID : ")
input_port = input("port : ")
# Start a new instance of Chrome web browser
driver = webdriver.Chrome()

# Open the website
driver.get("https://wikm.ir/frag/")

# Find and click the option that reveals additional options
protocol = driver.find_element(By.ID,"protocol")
protocol.click()

# Wait , find and click on option
wait = WebDriverWait(driver, 10)
specific_option = driver.find_element(By.XPATH,option)
specific_option.click()

# find , wait, click transmit
stream = driver.find_element(By.ID,"stream")
stream.click()
wait = WebDriverWait(driver,10)
stream = driver.find_element(By.XPATH,transmit)
stream.click()

# Find , type uuid
input_field = driver.find_element(By.ID,"uuid")
input_field.clear()
input_field.send_keys(uuid)

# port
port = driver.find_element(By.ID,"port")
port.clear()
port.send_keys(input_port)

# click on mux
mux = driver.find_element(By.XPATH,"/html/body/div[2]/div/label[4]")
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
