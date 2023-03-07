from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject import login_page
from Test.PageObject import service_page
from Common.parse_yml import ParseYml

host = ParseYml(file_path='Config', file_name='redmine.yml').parse_yml('website')


class TestService:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get(host['host'])
        # 登录
        login_page.LoginScenario(self.driver).login_success()
        time.sleep(3)
        self.service = service_page.ServiceScenario(self.driver)
        self.service_oper = service_page.ServiceOper(self.driver)

    def test_service_num(self):
        # 服务中运行任务数和递交任务数是否对应
        self.service.service_run_num()
        self.service_oper.click_dfx_analyise()
        time.sleep(5)

        # self.task_num = service_page.ServiceOper(self.driver).get_service_process_info()
        # assert ("3", self.task_num)

    def teardown(self):
        self.driver.quit()
