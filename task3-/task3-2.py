from selenium import webdriver

browser = webdriver.Chrome("C:/Users/21032/AppData/Local/Google/Chrome/Application/chromedriver.exe")
try:
    browser.get('https://mail.163.com/ ')
    method = browser.find_element_by_id('lbNormal')
    method.click()
    browser.switch_to.frame(0)
    input_email = browser.find_element_by_name('email')
    input_passwd = browser.find_element_by_name('password')
    btn_login = browser.find_element_by_id('dologin')
    input_email.send_keys('yqsyqsyqs')
    input_passwd.send_keys('123555aa')
    btn_login.click()

finally:
    pass