from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver

import time

from selenium.webdriver.common.by import By

driver : WebDriver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

def login():

    driver.maximize_window()
    driver.get("https://resume-filter-frontend-urtjok3rza-wl.a.run.app/login")
    # check assertion
    actual_title = driver.find_element(By.CSS_SELECTOR,'body > app-root > app-login > div > div.row.g-0 > div.col-md-8.col-lg-6 > div > div > div > div > h3').text
    print(actual_title)
    expected_title = 'Welcome back!'
    assert actual_title == expected_title
    driver.find_element(By.XPATH,value="//input[@type='emailAddress']").send_keys("divyanshi2000")
    time.sleep(2)
    driver.find_element(By.XPATH,value="//input[@type='password']").send_keys("Delhi@123")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,value="#rememberPasswordCheck").click()
    time.sleep(2)
    driver.find_element(By.XPATH,value="/html/body/app-root/app-login/div/div[2]/div[2]/div/div/div/div/form/div[4]/button").click()
    time.sleep(5)
    # check assertion
    actual_title = driver.find_element(By.CSS_SELECTOR,'body > app-root > app-dashboard > div > div.sub-header.container > div.heading').text
    print(actual_title)
    expected_title = 'Hire the finest'
    assert actual_title == expected_title

def Allrecruitment():

    driver.find_element(By.CSS_SELECTOR,value="#navbarNav > ul > li:nth-child(4) > a").click()
    time.sleep(5)
    driver.find_element(By.XPATH,value="/html/body/app-root/app-all-recruitments/div/div[2]/div/app-card[1]/div/div").click()
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR,value="#results").send_keys("C:\\Training period\\Manual product week\\score.csv")
    driver.find_element(By.CSS_SELECTOR,value="body > app-root > app-recruitment-completed > div.sub-header > div:nth-child(2) > button").click()
    # check assertion
    actual_title = driver.find_element(By.CSS_SELECTOR,'body > app-root > app-recruitment-completed > div.sub-header > div:nth-child(1) > div.heading').text
    print(actual_title)
    expected_title = 'test module'
    assert actual_title == expected_title
login()
Allrecruitment()
