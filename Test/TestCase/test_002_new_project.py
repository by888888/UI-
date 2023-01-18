from selenium import webdriver
import time, pytest
from Test.PageObject import login_page, project_new_page, add_task_dfx
from Common.parse_yml import parse_yml

host = parse_yml("../../Config/redmine.yml", "websites", "host")
url_1 = "http://" + host + "/redmine/login"
url_2 = "http://" + host + "/redmine/projects"
# 通过时间戳构造唯一项目名
project_name = 'project_{}'.format(time.time())
username = parse_yml("../../Config/redmine.yml", "logininfo", "username")
password = parse_yml("../../Config/redmine.yml", "logininfo", "password")


class TestNewProject():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问"登录"页面
        self.driver.get(url_1)
        # 登录
        login_page.LoginScenario(self.driver).login(username, password)

    def test_new_project(self):
        # 访问"项目列表"页面
        self.driver.get(url_2)
        # "新建项目"按钮
        project_list_page.ProjectListOper(self.driver).click_new_pro_btn()
        project_new_page.ProjectNewScenario(self.driver).new_project(project_name)
        # 新建项目成功后的提示信息
        text = project_new_page.ProjectNewOper(self.driver).get_pro_commit_info()
        assert text == '创建成功'

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', 'test_002_new_project.py'])
