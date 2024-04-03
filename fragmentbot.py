from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pyperclip
import time
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Use if running as root user
chrome_options.add_argument("--disable-dev-shm-usage")  # Use if running as root user
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/home/wikm/Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

##config Detector :

config_input = input("Enter your Config : ").lower()
uuid = "uuid"
SERVER = "google.com"
PORT = "443"
security = "tls"
transmit = "type" # example : ws
host = "subdomain.com"
PATH = "/admin"
SNI = "subdomain.com"
fingerprint = "chrome"
#type detect
type=config_input.split(":")[0]
NAME = config_input.split("#")[1]
if type == "vless" :
    uuid = config_input.split("@")[0].split("//")[1]
    SERVER = config_input.split("@")[1].split(":")[0]
    PORT = config_input.split("@")[1].split(":")[1].split("?")[0]
    sec2 = config_input.split("@")[1].split(":")[1].split("?")[1]
    sec2_list = sec2.split("&")
    print(sec2_list)
    count = len(sec2_list)
    for i in range(0,count) :
        str_sec2_list = str(sec2_list[i])
        if "security" in str_sec2_list :
            security = sec2_list[i].split("=")[1]
        # finde transmit
        elif transmit in str_sec2_list :
             transmit = sec2_list[i].split("=")[1]
        elif "host" in str_sec2_list : 
            host = sec2_list[i].split("=")[1]
        elif "path" in str_sec2_list :
            PATH = sec2_list[i].split("=")[1].split("%2f")[1]
        elif "sni" in str_sec2_list :
            SNI = sec2_list[i].split("=")[1]
        elif "fp" in str_sec2_list :
            fingerprint = sec2_list[i].split("=")[1]
        elif "alpn" in str_sec2_list :
            alpn = sec2_list[i].split("=")[1].split("#")[0]


print(security)
print(host)
print(fingerprint)
print(alpn)
#full-xpath
vless = "/html/body/div[2]/div/div[6]/select[1]/option[1]"
vmess = "/html/body/div[2]/div/div[6]/select[1]/option[2]"
trojan = "/html/body/div[2]/div/div[6]/select[1]/option[3]"
ws = "/html/body/div[2]/div/div[6]/select[2]/option[1]"
grpc = "/html/body/div[2]/div/div[6]/select[2]/option[2]"
#split
# config = input("enter your conf : ")
# c = config.split("&")
# type = c[0].split(":")[0]
# NAME = c[-1].split("#")[-1]
# SERVER = c[0].split("@")[1].split(':')[0]
# PORT = c[0].split("@")[1].split(':')[1].split("?")[0]
# uuid = c[0].split("@")[0].split("//")[1]
# SNI = c[5].split("=")[1]
# PATH = "/"+c[3].split(r"%2F")[1]
# transmit = c[1].split("=")[1]
##
if type == "vless" :
    type = vless
if type == "vmess" :
    type = vmess
if type == "trojan" :
    type = trojan

if transmit == "ws" : 
    transmit = ws
else : 
    transmit = grpc
# Start a new instance of Chrome web browser
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://wikm.ir/frag/")

# Find and click protocol
time.sleep(5)
protocol = driver.find_element(By.ID,"protocol")
protocol.click()
time.sleep(1)
specific_option = driver.find_element(By.XPATH,type)
specific_option.click()

# find , wait, click transmit
stream = driver.find_element(By.ID,"stream")
stream.click()
time.sleep(1)
stream = driver.find_element(By.XPATH,transmit)
stream.click()

# Find , type uuid
UID = driver.find_element(By.ID,"uuid")
UID.clear()
UID.send_keys(uuid)

# port
port = driver.find_element(By.ID,"port")
port.clear()
port.send_keys(PORT)

#address
cleanIp = driver.find_element(By.ID,"cleanIp")
cleanIp.clear()
cleanIp.send_keys(SERVER)

#sni
sni = driver.find_element(By.ID,"sni")
sni.clear()
sni.send_keys(SNI)

#path
path = driver.find_element(By.ID,"path")
path.clear()
path.send_keys(PATH)

# click on mux
mux = driver.find_element(By.XPATH,"/html/body/div[2]/div/label[4]")
mux.click()

# click on Early data
ed = driver.find_element(By.XPATH,"/html/body/div[2]/div/label[3]/strong")
ed.click()

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

#click on Download button
# time.sleep(5)
# download = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[21]/div/div/div[3]/button[3]")
# download.click()
# time.sleep(5)

#click on copy code :
time.sleep(5)
copy  = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[21]/div/div/div[3]/button[4]")
copy.click()
time.sleep(5)
copied_text = pyperclip.paste()
print(copied_text)

driver.quit()
