from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time

info = []

#Build webdriver with headless option, i.e no Chrome.exe window
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://publicrecordsrequests.iowa.uiowa.edu/salary")

try:
    #Find entry form and clear it
    search_box = driver.find_element(By.ID, "lastName")
    search_box.clear()

    #Specify last name to search for and send request
    search_box.send_keys("abcd")
    search_box.send_keys(Keys.RETURN)

    #Get HTML tag info for returned result
    page = driver.page_source
    soup = BeautifulSoup(page, features="html.parser")

    #Extract useful data
    child_soup = soup.find_all('h4')
    info = []

    for i in child_soup:
        #print('\33[33m' + i.text + '\33[0m')
        info.append(i.text)

    myName = info[0].split(",")
    name = myName[1] + " " + myName[0]

    title = info[1]
    findSalary = ""
    for tag in soup.find_all('p'):
        findSalary += str(tag)


    info.append(re.findall(r'<p> (\$[123456789].*)</p>', findSalary)[0])
    salary = info[2]

    print('\33[33m' + f'Name: {name} - Title: {title} - Salary: {salary}' + '\33[0m')

except:
    pass

################################################################################
driver.close
print("No data found. This window will close. Goodbye.")
time.sleep(10)

