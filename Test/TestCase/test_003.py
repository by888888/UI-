from selenium import webdriver
import time, pytest, allure, os
from Test.PageObject import login_page
from Common.parse_yml import parse_yml
from Common.parse_csv import parse_csv
from Common.get_project_path import get_project_path
from Test.PageObject import add_task_dfx

host_file = os.path.join(get_project_path(), "Config", "redmine.yml")
data_file = os.path.join(get_project_path(), "Data", "test_003.csv")
host = parse_yml(host_file, "website", "host")
data = parse_csv(data_file)


@pytest.mark.parametrize(("username", "password"), data)
class TestLogin():

    def test_login(self, username, password):
        self.driver = webdriver.Chrome("D:/chromedriver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get(host)
        # 登录
        login_page.LoginScenario(self.driver).login(username, password)
        add_task_dfx.AddTaskDfxOper(self.driver).click_add_task_start_btn()
        # add_task_dfx.AddTaskDfxOper(self.driver).click_upload_dragged_btn()
        add_task_dfx.AddTaskDfxOper(self.driver).input_file("C:\\Users\\Administrator\\Desktop\\ODB\\PCADEMODFM_V1.zip")
        add_task_dfx.AddTaskDfxOper(self.driver).click_rulegrop_btn()
        add_task_dfx.AddTaskDfxOper(self.driver).click_rulegrop_select()
        add_task_dfx.AddTaskDfxOper(self.driver).click_object_all_btn()
        add_task_dfx.AddTaskDfxOper(self.driver).click_add_task_finally_btn()
# #
# #
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_001_login.py'])
