from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://opensource-demo.orangehrmlive.com/'
s = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

try:
    driver.get(url)

    formFiller = driver.find_element(By.ID, 'txtUsername')
    formFiller.clear()
    formFiller.send_keys('Admin')

    formFiller = driver.find_element(By.ID, 'txtPassword')
    formFiller.clear()
    formFiller.send_keys('admin123')

    formFiller.send_keys(Keys.ENTER)

    driver.find_element(By.TAG_NAME, 'b').click()
    driver.find_element(By.ID, 'menu_admin_Job').click()
    driver.find_element(By.ID, 'menu_admin_viewJobTitleList').click()
    driver.find_element(By.ID, 'btnAdd').click()

    formFiller = driver.find_element(By.ID, 'jobTitle_jobTitle')
    formFiller.clear()
    formFiller.send_keys('Carpet washer')

    formFiller = driver.find_element(By.ID, 'jobTitle_jobDescription')
    formFiller.clear()
    formFiller.send_keys('The main duty is to wash carpets')

    formFiller = driver.find_element(By.ID, 'jobTitle_note')
    formFiller.clear()
    formFiller.send_keys('An important occupation for humanity')
    time.sleep(2)

    driver.find_element(By.ID, 'btnSave').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Carpet washer').click()
    time.sleep(2)
    driver.find_element(By.ID, 'btnSave').click()

    formFiller = driver.find_element(By.ID, 'jobTitle_jobDescription')
    formFiller.clear()
    formFiller.send_keys('VERSTAPPEN IS 2021 WORLD CHAMPION')
    time.sleep(2)

    driver.find_element(By.ID, 'btnSave').click()

    formFiller = driver.find_element(By.XPATH, "//*[contains(text(), 'Carpet washer')]").get_attribute('href')
    value = formFiller[(formFiller.index('=') + 1)::]
    qwe = "ohrmList_chkSelectRecord_"
    qwe += value
    driver.find_element(By.ID, qwe).click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="btnDelete"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="dialogDeleteBtn"]').click()
    time.sleep(5)

    try:
        driver.find_element(By.LINK_TEXT, 'Carpet washer')
    except NoSuchElementException:
        print('My Job is cleared')

    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
