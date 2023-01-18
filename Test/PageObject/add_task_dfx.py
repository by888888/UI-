'''
"项目列表"页面
'''
# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
from Common.parse_yml import parse_yml
username = parse_yml("../../Config/element.yml", "login", "username")
password = parse_yml('../../Config/element.yml', "login", "password")

# 页面对象层
class AddTaskDfx(object):

    def __init__(self, driver):
        self.driver = driver

    def find_add_task(self):
        ele = Base(self.driver).get_element(username)
        return ele


# 对象操作层
class ProjectListOper(object):
    def __init__(self, driver):
        self.project_list_page = ProjectListPage(driver)

    def click_new_pro_btn(self):
        self.project_list_page.find_new_pro_btn().click()

        # 业务逻辑层

    class ProjectListScenario(object):
        def __init__(self, driver):
            self.project_list_oper = ProjectListOper(driver)

        def xxx(self):
            # 目前不需要封装业务逻辑
            pass
