from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject import login_page
from Common.parse_csv import ParseCsv
from Test.PageObject import add_task_dfx

data_file = ParseCsv(file_path="Data", file_name="test_002_task_dfx.csv").parse_any_csv()


class TestAddDfxTask:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get("http://127.0.0.1:8081/#/login")
        # 登录
        login_page.LoginScenario(self.driver).login_success()
        time.sleep(2)
        self.add_dfx_task_odb = add_task_dfx.TaskDfxScenario(self.driver)
        self.add_dfx_task_oper = add_task_dfx.AddTaskDfxOper(self.driver)
        self.task_file = ParseCsv(file_path="Data", file_name="test_002_task_dfx.csv").parse_any_csv()

    def test_add_odb(self):
        # 递交任务
        # data = self.data
        self.add_dfx_task_odb.add_task_dfx_analysis(self.task_file)
        add_success = self.add_dfx_task_oper.get_add_task_success_info_text()
        assert ('DFX分析', add_success)

    def teardown(self):
        self.driver.quit()
