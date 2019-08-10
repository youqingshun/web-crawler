import time
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome("C:/Users/21032/AppData/Local/Google/Chrome/Application/chromedriver.exe")
url = 'http://mail.163.com/'
browser.get(url)
time.sleep(3)

browser.maximize_window()  # 打开网页窗口

time.sleep(5)

browser.switch_to.frame(0)  # 找到邮箱账号登录框对应的iframe,由于网页中iframe的id是动态的，所以不能用id寻找
print('7')
ActionChains(browser).move_by_offset(1210, 150).click().perform() # 鼠标右键点击
email = browser.find_element_by_name('email')  # 找到邮箱账号输入框
print('6')
email.send_keys('yqsyqsyqs')  # 将自己的邮箱地址输入到邮箱账号框中
print('1')
password = browser.find_element_by_name('password')  # 找到密码输入框
print('2')
password.send_keys('123555aa')  # 输入自己的邮箱密码
print('3')
login_em = browser.find_element_by_id('dologin')  # 找到登陆按钮
print('4')
login_em.click()  # 点击登陆按钮
print('5')
time.sleep(10)
