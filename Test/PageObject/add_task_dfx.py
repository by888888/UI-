'''
"项目列表"页面
'''
from selenium.webdriver import ActionChains
from Base.base import Base
from Common.parse_yml import parse_yml
import os
from Common.get_project_path import get_project_path

element = os.path.join(get_project_path(), "Config", "element.yml")
add_task_start = parse_yml(element, "dfx_task", "add_task_start")
upload_dragged = parse_yml(element, "dfx_task", "upload_dragged")
rulegrop = parse_yml(element, "dfx_task", "rulegrop")
rulegrop_select = parse_yml(element, "dfx_task", "rulegrop_select")
object_all = parse_yml(element, "dfx_task", "object_all")
add_task_finally = parse_yml(element, "dfx_task", "add_task_finally")
print(add_task_start)


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

    def find_rulegrop(self):
        ele = Base(self.driver).get_element(rulegrop)
        return ele

    def find_rulegrop_select(self):
        ele = Base(self.driver).get_element(rulegrop_select)
        return ele

    def find_object_all(self):
        ele = Base(self.driver).get_element(object_all)
        return ele

    def find_add_task_finally(self):
        ele = Base(self.driver).get_element(add_task_finally)
        return ele


# 页面元素操作层
class AddTaskDfxOper(object):
    def __init__(self, driver):
        self.add_task = AddTaskDfx(driver)
        self.driver = driver

    def click_add_task_start_btn(self):
        ele = self.add_task.find_add_task_start()
        ActionChains(self.driver).double_click(ele).perform()

    def click_upload_dragged_btn(self):
        ele = self.add_task.find_upload_dragged()
        ActionChains(self.driver).double_click(ele).perform()

    def input_file(self, file):
        # 对文本框做clear和send_keys操作
        self.add_task.find_upload_dragged().clear()
        self.add_task.find_upload_dragged().send_keys(file)

    def click_rulegrop_btn(self):
        ele = self.add_task.find_rulegrop()
        ActionChains(self.driver).double_click(ele).perform()

    def click_rulegrop_select(self):
        ele = self.add_task.find_rulegrop_select()
        ActionChains(self.driver).double_click(ele).perform()

    def click_object_all_btn(self):
        ele = self.add_task.find_object_all()
        ActionChains(self.driver).double_click(ele).perform()

    def click_add_task_finally_btn(self):
        ele = self.add_task.find_add_task_finally()
        ActionChains(self.driver).double_click(ele).perform()


# 页面业务场景层
class TaskDfxScenario(object):
    def __init__(self, driver):
        self.add_dfx_task = AddTaskDfxOper(driver)

    def add_task(self, file):
        # 定义一个递交任务的场景
        self.add_dfx_task.click_add_task_start_btn()
        self.add_dfx_task.click_upload_dragged_btn()
        self.add_dfx_task.input_file(file)
        self.add_dfx_task.click_rulegrop_btn()
        self.add_dfx_task.click_rulegrop_select()
        self.add_dfx_task.click_object_all_btn()
        self.add_dfx_task.click_add_task_finally_btn()

if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    from Test.PageObject import login_page
    driver = webdriver.Chrome("D:/chromedriver/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(20)
    # 访问"登录"页面
    driver.get("http://192.168.7.131:8081/#/login")
    # 登录
    login_page.LoginScenario(driver).login('admin', 'admin')

    file = 'C:\\Users\\Administrator\\Desktop\\ODB\\PCADEMODFM_V1.zip'
    TaskDfxScenario.add_task(driver,file)