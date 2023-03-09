from Common.get_project_path import get_project_path
import allure, os
from selenium import webdriver


class AssertScreen:

    def __init__(self, driver,file_path, file_name):
        self.png_path = os.path.join(get_project_path(), file_path, file_name)
        self.driver = driver
        # self.save_screenshot = webdriver.Chrome()

    def sreen_shot(self, expected_result, assert_result, screen_success_name, screen_fail_name):
        with allure.step("执行断言"):
            try:
                assert expected_result in assert_result
                self.driver.save_screenshot(self.png_path + screen_success_name)
                allure.attach.file(self.png_path + screen_success_name, attachment_type=allure.attachment_type.PNG)
            except:
                self.driver.save_screenshot(self.png_path + screen_fail_name)
                allure.attach.file(self.png_path + screen_fail_name, attachment_type=allure.attachment_type.PNG)
                # assert expected_result in assert_result

        # with allure.step("保存图片"):
        #     self.save_screenshot.save_screenshot(self.png_path + screen_success_name)
        #     allure.attach.file(self.png_path + screen_success_name, attachment_type=allure.attachment_type.PNG)

if __name__ == '__main__':
    pic_path = AssertScreen("Screenshot", "")
    pic_path.sreen_shot("DFX分析", "DFX分析", "sign_success01.png", "sign_fail01.png")

    # allure.attach.file("./pytest_study/image/pikaqiu.jpg", attachment_type=allure.attachment_type.JPG)