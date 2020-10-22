from selenium import webdriver
#from selenium.webdriver.common.Keys import Keys
import time

chrome_options = webdriver.ChromeOptions()

#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')

#driver.get('https://lms.unimelb.edu.au/canvas')
driver.get('https://canvas.lms.unimelb.edu.au/login/saml')

user_input = driver.find_element_by_id('usernameInput')
user_input.send_keys('hsingjungc')

password_input = driver.find_element_by_id('passwordInput')
password_input.send_keys('#9121oton')

btn_login = driver.find_element_by_css_selector('#top > div.page-inner > div > section > form > div:nth-child(3) > button')
btn_login.click()

btn_subject = driver.find_element_by_id('global_nav_courses_link')
btn_subject.click()

#driver.execute_script('var x = document.querySelectorAll("div.courseMediaIndicator capture");')
#driver.execute_script('if(x == null) alert("null");')
#driver.execute_script("return window.getComputedStyle(x[0], null")
#driver.execute_script("return window.getComputedStyle(arguments[1], ':before'")
path = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div[2]/div[11]/div/div/div/div[1]/div/div/div')
#path.click()

#driver.close()
