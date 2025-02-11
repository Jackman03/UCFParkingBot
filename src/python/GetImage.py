#File that takes a photo of the webparking map
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service
from datetime import datetime

#Funny default URL
url ='http://127.0.0.1:5500/src/html/map.html'

def TakeScreenshot():
    options = FirefoxOptions()
    service = Service(executable_path = '/snap/bin/firefox.geckodriver')
    print(options)
    driver = webdriver.Firefox(options=options, service=service)

    driver.get(url)
    now = datetime.now().strftime('%m-%d-%y %H:%M:%S')
    driver.save_screenshot(f'assets/MapScreenshots/ParkingMap.png')

    driver.quit()
TakeScreenshot()