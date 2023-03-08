import re
import time
from Base.base import Base
from Common.parse_yml import ParseYml
from Common.parse_csv import ParseCsv
from Common import public_method


# 查找定位元素
class LoginPage(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver
        self.element = ParseYml(file_path='Config', file_name='element.yml').parse_yml('login')

    def find_username(self):
        # 查找并返回"用户名"文本框元素
        ele = Base(self.driver).get_element(self.element['username'])
        return ele

    def find_password(self):
        # 查找并返回"密码"文本框元素
        ele = Base(self.driver).get_element(self.element['password'])
        return ele

    def find_login_btn(self):
        # 查找并返回"登录"按钮元素
        ele = Base(self.driver).get_element(self.element['login_submit'])
        return ele

    def find_login_name(self):
        # 查找并返回登录成功后的用户名元素
        ele = Base(self.driver).get_element(self.element['logging_text'])
        return ele

    def find_login_failed_info(self):
        # 查找并返回登录失败后的提示信息元素
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(self.element['flash_error'])
        return ele

    def find_login_out(self):
        # 查找退出元素
        ele = Base(self.driver).get_element(self.element['login_out'])
        return ele


# 页面元素操作层
class LoginOper(object):
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.login_page = LoginPage(driver)
        self.driver = driver
        self.public_method = public_method.public_method(driver)

    def input_username(self, username):
        # 对"用户名"文本框做clear和send_keys操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        # 对"密码"文本框做clear和send_keys操作
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def click_login_btn(self):
        self.public_method.click_btn(self.login_page.find_login_btn())

    def get_login_name(self):
        # 返回登录成功后的用户名元素
        return self.login_page.find_login_name().text

    def get_login_failed_info(self):
        # 返回登录失败后的提示信息元素
        return self.login_page.find_login_failed_info().text

    def click_login_out_btn(self):
        """
        :return: 点击退出
        """
        return self.public_method.click_btn(self.login_page.find_login_out())


# 页面业务场景层
class LoginScenario(object):
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.login_oper = LoginOper(driver)
        self.driver = driver

    def __get_data(self, row):
        """
        获取到测试数据
        :param row: 获取到第几行测试数据
        :return:
        """
        return ParseCsv(file_path="Data", file_name="test_001_login.csv").parse_specific_csv(row=row)

    def login_success(self):
        # 定义一个登录场景,登录成功
        data = self.__get_data(row=0)
        self.login_oper.input_username(data[0])
        self.login_oper.input_password(data[1])
        time.sleep(1)
        self.login_oper.click_login_btn()

    def login_fail(self):
        # 定义一个登录场景，登录失败
        data = self.__get_data(row=1)
        self.login_oper.input_username(data[0])
        self.login_oper.input_password(data[1])
        time.sleep(1)
        self.login_oper.click_login_btn()


# if __name__ == '__main__':
#     from selenium import webdriver
#
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     # 访问"登录"页面
#     driver.get("http://192.168.8.165:8081/#/login")
#     # 登录
#     c = "分析完成"
#     LoginScenario(driver).login_success()
#     # a = "class,el-table__row"
    # b = Base(driver).get_elements(a)
    # for i in b:
    #     data = re.findall(c, i.text)
    #     print(data)
