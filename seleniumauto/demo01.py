import time

from selenium import webdriver

# 运行在客户端
# 实例化driver
driver = webdriver.Remote('http://127.0.0.1:9515')
driver.implicitly_wait(20)  # 隐式等待

time.sleep(5)
driver.quit()

