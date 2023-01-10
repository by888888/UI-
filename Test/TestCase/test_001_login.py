from selenium import webdriver
import time, pytest, allure
from Test.PageObject import login_page
from Common.parse_yml import parse_yml

host = parse_yml("../../Config/redmine.yml", "website", "host")
host1 = parse_yml("../../Config/redmine.yml",'website','host')
# 通过时间戳构造唯一项目名
project_name = 'project_{}'.format(time.time())
username = parse_yml("../../Config/redmine.yml", "logininfo", "username")
password = parse_yml("../../Config/redmine.yml", "logininfo", "password")
print(host1)

# class TestNewProject():
#
#     def test_login(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(20)
#         # 访问"登录"页面
#         self.driver.get(host)
#         # 登录
#         login_page.LoginScenario(self.driver).login(username, password)
#         # 登录成功后的提示
#         login_success = login_page.LoginOper(self.driver).get_login_name()
#         login_failure = login_page.LoginOper(self.driver).get_login_failed_info()
#         assert login_success == '超级管理员'
#         assert login_failure == 'Vayo-DFX设计执行系统'
#         self.driver.close()
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_001_login.py'])
