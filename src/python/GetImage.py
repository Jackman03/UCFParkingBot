from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

url = 'http://127.0.0.1:5500/src/html/map.html'
driverpath = '/usr/local/bin'

driver = webdriver.Firefox()



driver.get(url)
 
driver.save_screenshot("image.png")

driver.quit()