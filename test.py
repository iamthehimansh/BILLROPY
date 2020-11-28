from selenium import webdriver
from time import sleep
chromedriver = r"C:\Users\IamTheHimansh\Documents\BILLROPY\static\chromedriver.exe"


driver = webdriver.Chrome(chromedriver)


driver.get("https://web.whatsapp.com/")
sleep(15)
driver.get("https://web.whatsapp.com/")