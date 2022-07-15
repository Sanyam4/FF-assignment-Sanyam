import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://in.investing.com/rates-bonds/euro-bund-historical-data')
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME,'login bold'),
            )
)

time.sleep(2)
driver.find_element(By.CLASS_NAME,'login bold').click()

login=driver.find_element(By.ID,'loginFormUser_email')
password=driver.find_element(By.ID,'loginForm_password')
login.send_keys('sanyammaheshwari3@gmail.com')
password.send_keys('FF1234')
driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/a').click()
WebDriverWait(driver, 50).until(
            EC.presence_of_element_located(
                (By.ID,'widgetField'),
            )
)
driver.find_element(By.ID,'widgetField').click()
startdate=driver.find_element(By.ID,'startDate')
startdate.click()
startdate.clear()
startdate.send_keys('01/01/2018')
enddate=driver.find_element(By.ID,'endDate')
enddate.click()
enddate.clear()
enddate.send_keys('15/06/2022')
driver.find_element(By.ID,'applyBtn').click()
time.sleep(2)
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[4]/section/div[8]/div[4]/div').click()




