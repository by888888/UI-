from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject import login_page
from Common.parse_yml import parse_yml
from Common.parse_csv import parse_csv
from Common.get_project_path import get_project_path

host_file = os.path.join(get_project_path(), "Config", "redmine.yml")
data_file = os.path.join(get_project_path(), "Data", "test_001_login.csv")
host = parse_yml(host_file, "website", "host")
data = parse_csv(data_file)


@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():

    def test_login(self, username, password, status):
        self.driver = webdriver.Chrome("D:/chromedriver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get(host)
        # 登录
        login_page.LoginScenario(self.driver).login(username, password)
        # 登录成功后的提示
        if status == '100':
            login_success = login_page.LoginOper(self.driver).get_login_name()
            assert login_success == 'DFX分析'
        elif status == '101':
            login_failure = login_page.LoginOper(self.driver).get_login_failed_info()
            assert login_failure == 'Vayo-DFX设计执行系统'
        self.driver.close()
# #
# #
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_001_login.py'])
