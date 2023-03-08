from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject import login_page
from Common.parse_yml import ParseYml
from Common.allure_assert import AssertScreen

host = ParseYml(file_path='Config', file_name='redmine.yml').parse_yml('website')


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get(host['host'])

    @allure.story("登录成功")
    def test_login_success(self):
        # 登录成功
        login_page.LoginScenario(self.driver).login_success()
        login_success = login_page.LoginOper(self.driver).get_login_name()
        AssertScreen(self.driver, "Screenshot", "").sreen_shot("DFX分析", login_success, "login_success_pass_01.png",
                                                               "login_success_fail_02.png")
    @allure.story("登录失败")
    def test_login_fail(self):
        # 登录失败
        login_page.LoginScenario(self.driver).login_fail()
        login_failure = login_page.LoginOper(self.driver).get_login_failed_info()
        AssertScreen(self.driver, "Screenshot", "").sreen_shot("Vayo-DFX设计执行系统", login_failure,
                                                               "login_fail_pass_01.png",
                                                               "login_fail_fail_01.png")
        # assert ('Vayo-DFX设计执行系统', login_failure)

    def teardown(self):
        self.driver.quit()
