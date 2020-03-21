# ---essential modules---
import os
import time
from datetime import datetime as dt
# ---essential modules---

hosts = os.getcwd() + '\hosts'   #temporary file for testing
host_path = r'C:\Windows\System32\drivers\etc\hosts' #windows
redirect = '127.0.0.1'   # redirect web_path
websites = ["www.instagram.com","www.snapchat.com","www.facebook.com", "www.bing.com", "www.youtube.com", "www.pronhub.com"]   #website that you want to block


current = dt.now()   # for getting the current day information, like day, month, year, hours, minutes, seconds, micro-second

while True:
    if dt(current.year, current.month, current.day, 8) < dt.now() < dt(current.year, current.month, current.day,16):   #checking if the time is between 8am --> 4pm
        print('Working Hours....')
        with open(host_path, 'r+') as file:    
            content = file.read()
            for sites in websites:
                if sites in content:   # checking if the websites are already mentioned
                    pass
                else:
                    block = redirect + " " + sites + '\n'   # add "127.0.0.1 www.website.com" to the file
                    file.write(block)

    else:   # if the time is to relax
        print('Fun time.....')
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)  #takes the cursor to the top of the file
            for lines in content:
                if not any(website in lines for website in websites):   # checking if the websites are already mentioned in the host file
                    file.write(lines) #writting
                file.truncate()   #deletes the text below the already written text
    time.sleep(15)   #excetuting the condition for after every 15 seconds