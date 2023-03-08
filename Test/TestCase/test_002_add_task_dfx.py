from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject.login_page import LoginScenario
from Common.parse_csv import ParseCsv
from Test.PageObject.add_task_dfx import TaskDfxScenario,AddTaskDfxOper
from Common.parse_yml import ParseYml
from Common.allure_assert import AssertScreen

host = ParseYml(file_path='Config', file_name='redmine.yml').parse_yml('website')


# data_file = ParseCsv(file_path="Data", file_name="test_002_task_dfx.csv").parse_any_csv()

@allure.story('DFX任务')
class TestAddDfxTask(LoginScenario,TaskDfxScenario,AddTaskDfxOper):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get(host['host'])
        # 登录
        LoginScenario(self.driver).login_success()
        time.sleep(2)
        self.task_file = ParseCsv(file_path="Data", file_name="test_002_task_dfx.csv").parse_any_csv()

    @allure.story("递交ODB数据")
    def test_add_odb(self):
        TaskDfxScenario(self.driver).add_task_dfx_analysis(self.task_file)
        add_success = AddTaskDfxOper(self.driver).get_add_task_success_info_text()
        AssertScreen(self.driver, "Screenshot", "").sreen_shot("DFX分析", add_success, "add_odb_success_pass_01.png",
                                                               "add_odb_success_fail_02.png")

    def teardown(self):
        self.driver.quit()
