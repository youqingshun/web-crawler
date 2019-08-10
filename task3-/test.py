# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:/Users/21032/AppData/Local/Google/Chrome/Application/chromedriver.exe")
driver.get("http://www.baidu.com")# 访问百度

# 设置浏览器窗口大小
driver.set_window_size(620, 600)  # 报错
# driver.maximize_window()           # 正常（窗口设置大一点也正常）
#####################百度输入框的定位方式########################

# 通过 id 方式定位
driver.find_element_by_id("kw").send_keys("selenium")

# 通过 name 方式定位
# driver.find_element_by_name("wd").send_keys("selenium")

# 通过 tag name 方式定位
# driver.find_element_by_tag_name("input").send_keys("selenium")

# 通过 class name 方式定位
# driver.find_element_by_class_name("s_ipt").send_keys("selenium")

# 通过 CSS 方式定位
# driver.find_element_by_css_selector("#kw").send_keys("selenium")

# 通过 xpath 方式定位
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

###################################################################

# 点击搜索按钮
# driver.find_element_by_id("su").click()
driver.find_element_by_id("su").send_keys(Keys.ENTER)
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(200,400);"
driver.execute_script(js)
sleep(5)

# 退出浏览器
driver.quit()
