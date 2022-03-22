import logging
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

dataArray = [
  {
    "Phone Number": "40716543298",
    "First Name": "John",
    "Last Name": "Smith",
    "Company Name": "IT Solutions",
    "Role in Company": "Analyst",
    "Address": "98 North Road",
    "Email": "jsmith@itsolutions.co.uk",
  },
  {
    "Phone Number": "40791345621",
    "First Name": "Jane",
    "Last Name": "Dorsey",
    "Company Name": "MediCare",
    "Role in Company": "Medical Engineer",
    "Address": "11 Crown Street",
    "Email": "jdorsey@mc.com",
  },
  {
    "Phone Number": "40735416854",
    "First Name": "Albert",
    "Last Name": "Kipling",
    "Company Name": "Waterfront",
    "Role in Company": "Accountant",
    "Address": "22 Guild Street",
    "Email": "kipling@waterfront.com",
  },
  {
    "Phone Number": "40733652145",
    "First Name": "Michael",
    "Last Name": "Robertson",
    "Company Name": "MediCare",
    "Role in Company": "IT Specialist",
    "Address": "17 Farburn Terrace",
    "Email": "mrobertson@mc.com",
  },
  {
    "Phone Number": "40799885412",
    "First Name": "Doug",
    "Last Name": "Derrick",
    "Company Name": "Timepath Inc.",
    "Role in Company": "Analyst",
    "Address": "99 Shire Oak Road",
    "Email": "dderrick@timepath.co.uk",
  },
  {
    "Phone Number": "40733154268",
    "First Name": "Jessie",
    "Last Name": "Marlowe",
    "Company Name": "Aperture Inc.",
    "Role in Company": "Scientist",
    "Address": "27 Cheshire Street",
    "Email": "jmarlowe@aperture.us",
  },
  {
    "Phone Number": "40712462257",
    "First Name": "Stan",
    "Last Name": "Hamm",
    "Company Name": "Sugarwell",
    "Role in Company": "Advisor",
    "Address": "10 Dam Road",
    "Email": "shamm@sugarwell.org",
  },
  {
    "Phone Number": "40731254562",
    "First Name": "Michelle",
    "Last Name": "Norton",
    "Company Name": "Aperture Inc.",
    "Role in Company": "Scientist",
    "Address": "13 White Rabbit Street",
    "Email": "mnorton@aperture.us",
  },
  {
    "Phone Number": "40741785214",
    "First Name": "Stacy",
    "Last Name": "Shelby",
    "Company Name": "TechDev",
    "Role in Company": "HR Manager",
    "Address": "19 Pineapple Boulevard",
    "Email": "sshelby@techdev.com",
  },
  {
    "Phone Number": "40731653845",
    "First Name": "Lara",
    "Last Name": "Palmer",
    "Company Name": "Timepath Inc.",
    "Role in Company": "Programmer",
    "Address": "87 Orange Street",
    "Email": "lpalmer@timepath.co.uk",
  },
]

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def fillData (driver: webdriver.Chrome, data):
  driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')
  driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelPhone"]').send_keys(data["Phone Number"])
  driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelLastName"]').send_keys(data["Last Name"])
  driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelEmail"]').send_keys(data["Email"])
  driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelCompanyName"]').send_keys(data["Company Name"])
  driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelRole"]').send_keys(data["Role in Company"])
  driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelAddress"]').send_keys(data["Address"])
  driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelFirstName"]').send_keys(data["First Name"])
  driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]').click()

def main():
  driver = webdriver.Chrome(options=set_chrome_options()) 
  driver.maximize_window()
  driver.implicitly_wait(15)
  driver.get('https://www.rpachallenge.com/')
  for i in dataArray: 
    fillData(driver, i)
  # driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')

    

if __name__ == "__main__":
    main()