from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('C:\\Users\\hp\\Downloads\\chromedriver_win32 (4)\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
driver.find_element("link text", "nav-link")
driver.find_element_by_xpath("//input[@id='Username']").send_keys("sam muraga")
driver.find_element_by_xpath("//input[@id='Password']").send_keys("manik@123")
driver.find_element_by_xpath("//input[@name='login']").click()
