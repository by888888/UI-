import time
from Base.base import Base
from Common.parse_yml import ParseYml
import re
from Common.public_method import public_method
from Common.parse_csv import ParseCsv
from Test.PageObject import add_task_dfx


# 查找定位元素
class ServicePage(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver
        self.element = ParseYml(file_path='Config', file_name='element.yml').parse_yml('service')

    def find_process_num(self):
        # 查找状态中：分析中的个数元素
        ele = Base(self.driver).get_elements(self.element['process_num'])
        return ele

    def find_service_menu_1(self):
        # 查找服务的菜单的元素
        ele = Base(self.driver).get_element(self.element['service_menu_1'])
        return ele

    def find_service_menu_2(self):
        # 查找二级服务菜单的元素
        ele = Base(self.driver).get_element(self.element['service_menu_2'])
        return ele

    def find_task_process(self):
        # 查找正在进行的任务数元素
        ele = Base(self.driver).get_element(self.element['task_process'])
        return ele

    def find_service_ip(self):
        # 查找服务中的ip文本
        # ele = self.driver.find_element_by_id('loggedas')
        ele = Base(self.driver).get_element(self.element['service_ip'])
        return ele

    def find_dfx_analyise(self):
        # 查找任务菜单栏中的DFX任务元素
        ele = Base(self.driver).get_element(self.element['dfx_analyise'])
        return ele


# 页面元素操作层
class ServiceOper(object):
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.service_page = ServicePage(driver)
        self.driver = driver
        self.public_method = public_method(driver)

    def get_process_num_info(self, value):
        # 获取状态为分析中的个数
        new_list = []
        for i in (self.service_page.find_process_num()):
            data = re.findall(value, i.text)
            for j in data:
                new_list.append(list(filter(None, j)))
        return len(new_list)

    def click_service_menu_1(self):
        # 对服务菜单进行点击
        self.public_method.click_btn(self.service_page.find_service_menu_1())

    def click_service_menu_2(self):
        # 对下拉后的服务进行点击
        self.public_method.click_btn(self.service_page.find_service_menu_2())

    def get_service_process_info(self):
        # 获取服务中的正在进行的任务数量
        return self.service_page.find_task_process().text

    def get_service_ip_info(self):
        # 获取服务中的ip地址
        return self.service_page.find_service_ip().text

    def click_dfx_analyise(self):
        # 对下拉后的服务进行点击
        self.public_method.click_btn(self.service_page.find_dfx_analyise())


# 页面业务场景层
class ServiceScenario(object):
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.driver = driver
        self.service_oper = ServiceOper(driver)
        self.__get_data = ParseCsv(file_path="Data", file_name="test_003_service_num.csv").parse_any_csv()
        self.__add_task = add_task_dfx.TaskDfxScenario(self.driver)

    def service_run_num(self):
        # 获取当前运行的任务数量
        self.__add_task.add_task_dfx_analysis(self.__get_data)
        # while self.service_oper.get_process_num_info("分析中"self.__get_data) == len(self.__get_data):
        self.service_oper.click_service_menu_1()
        self.service_oper.click_service_menu_2()
        self.service_oper.get_service_ip_info()
        while True:
            if self.service_oper.get_service_process_info() == len(self.__get_data):
                break
            else:
                self.service_oper.get_service_ip_info()
                time.sleep(2)
                self.service_oper.get_service_process_info()
                self.driver.refresh()
