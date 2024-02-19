config = input("enter your conf : ")
config = str(config)
c = config.split("&")
type = c[0].split(":")[-1]
NAME = c[-1].split("#")[-1]
SERVER = c[0].split("@")[1].split(':')[0]
PORT = c[0].split("@")[1].split(':')[1].split("?")[0]
UID = c[0].split("@")[0].split("//")[1]
SNI = c[5].split("=")[1]
PATH = c[3].split(r"%2F")[1]
stream = c[1].split("=")[1]
PROXY = '{"name":"NAME","type":"vless","server":"SERVER","port":PORT,"uuid":"UUID","tls":true,"servername":"SNI","network":"ws","ws-opts":{"path":"/PATH","headers":{"host":"SNI"}}}'.replace("NAME",NAME).replace("SERVER",SERVER).replace("PORT",PORT).replace("UUID",UID).replace("SNI",SNI).replace("PATH",PATH)
print ("---------------------------------------------")
print(PROXY)