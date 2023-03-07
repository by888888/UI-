from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject import login_page
from Common.parse_yml import ParseYml
host = ParseYml(file_path='Config', file_name='redmine.yml').parse_yml('website')


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get(host['host'])
        self.login_dfx = login_page.LoginScenario(self.driver)
        self.login_dfx_text = login_page.LoginOper(self.driver)

    def test_login_success(self):
        # 登录成功
        self.login_dfx.login_success()
        login_success = self.login_dfx_text.get_login_name()
        assert ('DFX分析', login_success)

    def test_login_fail(self):
        # 登录失败
        self.login_dfx.login_fail()
        login_failure = login_page.LoginOper(self.driver).get_login_failed_info()
        assert ('Vayo-DFX设计执行系统', login_failure)

    def teardown(self):
        self.driver.quit()
