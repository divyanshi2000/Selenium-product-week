from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

from selenium.webdriver.common.by import By


def signup():
    driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://resume-filter-frontend-urtjok3rza-wl.a.run.app/signup")
    # check assertion
    actual_title = driver.find_element(By.CSS_SELECTOR,'body > app-root > app-sign-up > div > div.right > div.signup').text
    print(actual_title)
    expected_title = 'Sign Up'
    assert actual_title == expected_title
    driver.find_element(By.XPATH,value="//input[@type='text']").send_keys("maria")
    time.sleep(2)
    driver.find_element(By.XPATH,value="//input[@type='email']").send_keys("maria20@yopmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH,value="//input[@class='form-control ng-untouched ng-pristine ng-invalid']").send_keys("maria200")
    time.sleep(2)
    driver.find_element(By.XPATH,value="//input[@type='password']").send_keys("Delhi@123")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'body > app-root > app-sign-up > div > div.right > form > div:nth-child(5) > input').send_keys("Delhi@123")
    time.sleep(2)
    drp=Select(driver.find_element(By.XPATH,value="/html/body/app-root/app-sign-up/div/div[3]/form/div[6]/select"))
    time.sleep(2)
    drp.select_by_visible_text('Subject Expert')
    time.sleep(2)
    driver.find_element(By.XPATH, value="/html/body/app-root/app-sign-up/div/div[3]/form/div[7]/input").send_keys("python")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, value="body > app-root > app-sign-up > div > div.right > form > div.mb-3.form-check > input").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, value="body > app-root > app-sign-up > div > div.right > form > button").click()
    time.sleep(5)
    # check assertion
    actual_title = driver.find_element(By.CSS_SELECTOR,'body > app-root > app-expert-dashboard > div.sub-header.container > div.heading').text
    print(actual_title)
    expected_title = 'Recruitment'
    assert actual_title == expected_title



signup()