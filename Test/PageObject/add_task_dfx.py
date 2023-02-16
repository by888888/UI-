'''
"项目列表"页面
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from Base.base import Base
from Common.parse_yml import parse_yml
import os, time
from Common.get_project_path import get_project_path
from Common import public_method

element = os.path.join(get_project_path(), "Config", "element.yml")
add_task_start = parse_yml(element, "dfx_task", "add_task_start")
upload_dragged = parse_yml(element, "dfx_task", "upload_dragged")
last_selection = parse_yml(element, "dfx_task", "last_selection")
rulegrop = parse_yml(element, "dfx_task", "rulegrop")
rulegrop_select = parse_yml(element, "dfx_task", "rulegrop_select")
object_all = parse_yml(element, "dfx_task", "object_all")
add_task_finally = parse_yml(element, "dfx_task", "add_task_finally")
object_text = parse_yml(element, "dfx_task", "object_text")
add_task_success_info = parse_yml(element, "dfx_task", "add_task_success_info")
object_all_point = parse_yml(element, "dfx_task", "object_all_point")


# print(add_task_start)


# 查找定位元素
class AddTaskDfx(object):

    def __init__(self, driver):
        self.driver = driver

    def find_add_task_start(self):
        ele = Base(self.driver).get_element(add_task_start)
        return ele

    def find_upload_dragged(self):
        ele = Base(self.driver).get_element(upload_dragged)
        return ele

    def find_last_selection(self):
        ele = Base(self.driver).get_element(last_selection)
        return ele

    def find_rulegrop(self):
        ele = Base(self.driver).get_element(rulegrop)
        return ele

    def find_rulegrop_select(self):
        ele = Base(self.driver).get_element(rulegrop_select)
        return ele

    def find_object_all(self):
        ele = Base(self.driver).get_element(object_all)
        return ele

    def find_object_text(self):
        ele = Base(self.driver).get_element(object_text)
        return ele

    def find_add_task_finally(self):
        ele = Base(self.driver).get_element(add_task_finally)
        return ele

    def find_add_task_success_info(self):
        ele = Base(self.driver).get_element(add_task_finally)
        return ele

    def find_object_all_point(self):
        ele = Base(self.driver).get_element(object_all_point)
        return ele


# 页面元素操作层
class AddTaskDfxOper(object):
    def __init__(self, driver):
        self.add_task = AddTaskDfx(driver)
        self.driver = driver

    # 递交任务
    def click_add_task_start_btn(self):
        ele = self.add_task.find_add_task_start()
        ActionChains(self.driver).click(ele).perform()

    # 上传文件
    def input_file(self, file):
        # 对文本框做clear和send_keys操作
        # self.add_task.find_upload_dragged().clear()
        self.add_task.find_upload_dragged().send_keys(file)

    # 上一次选择否
    def click_last_selection_btn(self):
        ele = self.add_task.find_last_selection()
        ActionChains(self.driver).click(ele).perform()

    # 选择规则集
    def click_rulegrop_btn(self):
        ele = self.add_task.find_rulegrop()
        ActionChains(self.driver).click(ele).perform()

    # 选择对应的规则
    def click_rulegrop_select(self):
        ele = self.add_task.find_rulegrop_select()
        ActionChains(self.driver).click(ele).perform()

    # 选择全部
    def click_object_all_btn(self):
        ele = self.add_task.find_object_all()
        ActionChains(self.driver).click(ele).perform()

    # 最后递交任务
    def click_add_task_finally_btn(self):
        ele = self.add_task.find_add_task_finally()
        ActionChains(self.driver).click(ele).perform()

    # 查找递交任务后的元素
    def get_add_task_success_info_text(self):
        return self.add_task.find_add_task_success_info().text()


# 页面业务场景层
class TaskDfxScenario(object):
    def __init__(self, driver):
        self.add_dfx_task = AddTaskDfxOper(driver)
        self.find_task_element = AddTaskDfx(driver)
        self.public_method = public_method.public_method(driver)

    def add_task(self, file):
        # 定义一个递交任务的场景
        self.add_dfx_task.click_add_task_start_btn()
        self.add_dfx_task.input_file(file)
        # 等待最后一次选择的出现
        self.public_method.show_wait(self.find_task_element.find_last_selection())
        self.add_dfx_task.click_last_selection_btn()
        self.public_method.scroll_height(object_text)
        time.sleep(2)
        self.add_dfx_task.click_rulegrop_btn()
        self.public_method.show_wait(self.find_task_element.find_rulegrop_select())
        self.add_dfx_task.click_rulegrop_select()
        self.add_dfx_task.click_object_all_btn()
        self.public_method.show_wait(self.find_task_element.find_object_all_point())
        self.add_dfx_task.click_add_task_finally_btn()
        self.public_method.show_wait(self.find_task_element.find_add_task_success_info())



# if __name__ == '__main__':
#     from selenium import webdriver
#     from time import sleep
#     from Test.PageObject import login_page
#     driver = webdriver.Chrome("D:/chromedriver/chromedriver.exe")
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     # 访问"登录"页面
#     driver.get("http://192.168.7.131:8081/#/login")
#     # 登录
#     login_page.LoginScenario(driver).login('admin', 'admin')
#
#     file = 'C:\\Users\\Administrator\\Desktop\\ODB\\PCADEMODFM_V1.zip'
#     TaskDfxScenario.add_task(driver,file)
