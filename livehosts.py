import requests
import sys
from threading import Thread


class colors: 
    reset='\033[0m'
    class fg: 
        red='\033[31m'
        orange='\033[33m'
        blue='\033[34m'
        yellow='\033[93m'
        pink='\033[95m'


file = sys.argv[1]
templist = []
threads = []
livehosts = []


print colors.fg.yellow + "===========Alive Hosts==========	-Adwaith" + colors.reset

def connect(line,livehosts):	
	sub1 = "https://" + line
	sub2 = "http://" + line
	sub1 = sub1.rstrip()
	sub2 = sub2.rstrip()

	try:
		https = requests.get(sub1)
		httpsstatus = https.status_code
	except Exception:
		return
	if httpsstatus == 200:
		print colors.fg.orange + sub1 + colors.reset 
		livehosts.append(sub1)

	try:
		http = requests.get(sub2)
		httpstatus = http.status_code
	except Exception:
		return
	if httpstatus == 200:
		print colors.fg.blue + sub2 + colors.reset
		livehosts.append(sub2)

print colors.fg.pink + "[+] Fetching subdomains from {0}".format(file) + colors.reset


filecontent = open(file, "r")

for line in filecontent:
	templist.append(line)
	
for i in range(len(templist)):
	line = templist[i].replace("'", "")
	process = Thread(target=connect, args=[line,livehosts])
	process.start()
	threads.append(process)

for process in threads:
	process.join()

print colors.fg.yellow + "[+] Saving results to livehosts.txt" + colors.reset
file = open("livehosts.txt",'w')
for i in range(len(livehosts)):
	file.write(livehosts[i])
	file.write("\n")
file.close()
