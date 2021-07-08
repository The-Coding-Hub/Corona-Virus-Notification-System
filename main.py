# Programme Topic: Corona Virus Notification System using Python

import requests # Importing requests module in Python
from bs4 import BeautifulSoup # Importing BeautifulSoup class from the bs4 module
from plyer import notification # Importing notification class from the plyer module to show notifications

# Getting the main html source code from the required website

url = "https://www.mohfw.gov.in/"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, "html.parser")

# Getting Data

vac = soup.find("span", class_="totalvac").get_text() # "Total Vaccination" 
vac_num = soup.find("span", class_="coviddata").get_text() # "<number>"

data = soup.find_all("span", class_="mob-show")
text_main = []
for text in data:
	text_main.append(text.get_text())

# Getting required text from the created list

active = text_main[0]
active_num = text_main[2]
discharged = text_main[3]
discharged_num = text_main[5]
death = text_main[6]
death_num = text_main[8]

active = active + ": " + active_num # Active Text + Number
discharged = discharged + ": " + discharged_num # Discharged Text + Number
death = death + ": " + death_num # Death Text + Number

# Sending Notification

notification.notify(title = "Corona Virus Update", 
	message = vac + vac_num + "\n" + active + "\n" + discharged + "\n" + death, 
	app_icon = "icon.ico",
	timeout = 10
)