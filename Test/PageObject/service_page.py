'''
登录页面
'''
# 页面元素对象层
import time

from selenium.webdriver import ActionChains
from Base.base import Base
from Common.parse_yml import parse_yml
from Common.get_project_path import get_project_path
import os

element = os.path.join(get_project_path(), "Config", "element.yml")
service_menu_1 = parse_yml(element, "service", "service_menu_1")
service_menu_2 = parse_yml(element, "service", "service_menu_2")
task_process = parse_yml(element, "service", "task_process")
service_ip = parse_yml(element, "service", "service_ip")


# 查找定位元素
class ServicePage(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_service_menu_1(self):
        # 查找并返回"用户名"文本框元素
        # ele = self.driver.find_element_by_id('username')
        # ele = self.driver.find_element_by_name('username')
        ele = Base(self.driver).get_element(service_menu_1)
        return ele

    def find_service_menu_2(self):
        # 查找并返回"密码"文本框元素
        # ele = self.driver.find_element_by_id('password')
        ele = Base(self.driver).get_element(service_menu_1)
        return ele

    def find_task_process(self):
        # 查找并返回"登录"按钮元素
        # ele = self.driver.find_element_by_id('login-submit')
        ele = Base(self.driver).get_element(task_process)
        return ele

    def find_service_ip(self):
        # 查找并返回登录成功后的用户名元素
        # ele = self.driver.find_element_by_id('loggedas')
        ele = Base(self.driver).get_element(service_ip)
        return ele


# 页面元素操作层
class ServiceOper(object):
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.service_page = ServicePage(driver)
        self.driver = driver

    def click_service_menu_1(self):
        # 对服务菜单进行点击
        ele = self.service_page.find_service_menu_1()
        ActionChains(self.driver).click(ele).perform()

    def click_service_menu_2(self):
        # 对下拉后的服务进行点击
        ele = self.service_page.find_service_menu_2()
        ActionChains(self.driver).click(ele).perform()

    def get_task_process_info(self):
        # 获取服务中的正在进行的任务数量
        return self.service_page.find_task_process().text

    def get_service_ip_info(self):
        # 获取服务中的ip地址
        return self.service_page.find_service_ip().text



# 页面业务场景层
class LoginScenario(object):
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.login_oper = LoginOper(driver)

    def login(self, username, password):
        # 定义一个登录场景，用到了3个操作
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        # self.login_oper.input_verification_code()
        self.login_oper.click_login_btn()
        time.sleep(1)
