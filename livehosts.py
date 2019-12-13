import requests
import sys
import time

file = sys.argv[1]
templist = []


print "===========Alive Hosts==========	-Adwaith"

def connect(line):	

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
		print sub1 

	try:
		http = requests.get(sub2)
		httpstatus = http.status_code
	except Exception:
		return
	if httpstatus == 200:
		print sub2


filecontent = open(file, "r")

for line in filecontent:
	templist.append(line)
	
for i in range(len(templist)):
	line = templist[i].replace("'", "")
	connect(line)

