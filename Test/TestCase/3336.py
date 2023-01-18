'''
登录页面
'''
# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
from Common.parse_yml import parse_yml
import pytest

username = parse_yml("../../Config/element.yml", "css", "username")
password = parse_yml('../../Config/element.yml', "css", "password")
# print(password)
# login-submit = parse_yml("../../Config/element.yml", "class","login-submit")
login_submit = parse_yml("../../Config/element.yml", "css", "login_submit")
logging_text = parse_yml("../../Config/element.yml", "css", "logging_text")
flash_error = parse_yml("../../Config/element.yml", "css", "flash_error")





# if __name__ == '__main__':
#     p = LoginPage(object)
#
#     print(ele)

class LoginPage(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_username(self):
        # 查找并返回"用户名"文本框元素
        # ele = self.driver.find_element_by_id('username')
        # ele = self.driver.find_element_by_name('username')
        ele = Base(self.driver).get_element('css,username')
        return ele


    def find_password(self):
        # 查找并返回"密码"文本框元素
        # ele = self.driver.find_element_by_id('password')
        ele = Base(self.driver).get_element('css,password')
        return ele

    def find_login_btn(self):
        # 查找并返回"登录"按钮元素
        # ele = self.driver.find_element_by_id('login-submit')
        ele = Base(self.driver).get_element('css,login_submit')
        return ele

    def find_login_name(self):
        # 查找并返回登录成功后的用户名元素
        # ele = self.driver.find_element_by_id('loggedas')
        ele = Base(self.driver).get_element('css,logging_text')
        return ele

    def find_login_failed_info(self):
        # 查找并返回登录失败后的提示信息元素
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element('css,flash_error')
        return ele

    # def find_verification_code(self):
    #       ele = self.driver.find_element_by_id('aaa')
    #       return ele