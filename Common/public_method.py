# 公用的封装方法
import re

from selenium import webdriver
from time import sleep
from Base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class public_method:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 拉直最底部
    def scroll_height(self, element):
        ele = self.driver.execute_script("arguments[0].scrollIntoView();", Base(self.driver).get_element(element))
        return ele

    # 显示等待
    def show_wait(self, element):
        ele = WebDriverWait(self.driver, 20).until(lambda x: element.is_displayed())
        return ele

    # 单击btn
    def click_btn(self, element):
        return ActionChains(self.driver).click(element).perform()





# driver = webdriver.Chrome()
# url = 'http://www.sogou.com'
# driver.get(url)
# time.sleep(2)
#
# input_box = driver.find_element_by_id('query')  # 获取需要等待的元素
# visibility_by_element(input_box)  # 调用自定义封装的方法进行显式等待
# visibility_by_xpath("//input[@id='query']")  # 调用自定义封装的方法进行显式等待
# input_box.send_keys('天天向上')
# button = clickable(By.ID, 'stb')  # 调用自定义封装的方法进行显式等待
# button.click
# time.sleep(3)
# driver.close()

# 显示等待
# driver = webdriver.Chrome()
# driver.get('http://192.168.7.131:8081/#/login')
# driver.maximize_window()
# a = "css,.user-input > input:nth-child(1)"
# b = "css,div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
# c = "css,.el-button"
# d = "xpath,/html/body/div/section/section/main/div/div/div[1]/button"
# e = "xpath,/html/body/div[1]/section/section/main/div[1]/div[2]/div/form/div[9]/span"
# bp = Base(driver)
# p1 = bp.get_element(a).send_keys('admin')
# p2 = bp.get_element(b).send_keys('admin')
# p3 = bp.get_element(c).click()
# sleep(2)
# p4 = bp.get_element(d).click()
# sleep(2)
# print("Start_____")
# # driver.execute_script("document.documentElement.scrollTop=10000")
# driver.execute_script("arguments[0].scrollIntoView();", bp.get_element(e))
# # driver.execute_script("window.scrollTo(0,10000)")
