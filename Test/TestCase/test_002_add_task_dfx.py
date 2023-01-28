from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject import login_page
from Common.parse_csv import parse_csv
from Test.PageObject import add_task_dfx
from Common.get_project_path import get_project_path

file_path = os.path.join(get_project_path(), "Data", "test_002_task_dfx.csv")
file = parse_csv(file_path)


# # 通过时间戳构造唯一项目名
# project_name = 'project_{}'.format(time.time())
@pytest.mark.parametrize(("file"), file)
class TestAddTaskDfx:
    def setup(self):
        self.driver = webdriver.Chrome("D:/chromedriver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get("http://192.168.7.131:8081/#/login")
        # 登录
        login_page.LoginScenario(self.driver).login('admin', 'admin')

    def test_add_odb(self, file):
        # 递交任务
        add_task_dfx.TaskDfxScenario(self.driver).add_task(file)


    def teardown(self):
        self.driver.quit()
