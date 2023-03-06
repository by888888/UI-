from selenium.webdriver.support.ui import WebDriverWait

'''
这里我们定义一个名为"Base"的类，对Selenium WebDriver提供的API进行二次封装
'''


class Base(object):
    def __init__(self, driver):
        '''
        调用该类的时候给其传递一个driver
        :param driver:
        '''
        self.driver = driver

    def split_locator(self, locator):
        '''
        分解定位表达式，如"id,kw"，拆分后返回定位器"id"和定位器的值"kw"
        :param locator: 定位方法+定位表达式组合字符串，如"id,kw"
        :return: locator_dict[by], value：返回定位方式和定位表达式
        '''
        if len(locator.split(',')) == 3:
            by = locator.split(',')[0]  # 定位器
            value = locator.split(',')[1] + ',' + locator.split(',')[2]
        else:
            by = locator.split(',')[0]  # 定位器
            value = locator.split(',')[1]  # 定位器值
        # 这里是为了方便，所以简写了定位器
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            raise NameError("Locator Err!'id',only 'name','class','tag','link','plink', 'xpath','css' can be used.")
        return locator_dict[by], value

    def get_element(self, locator, sec=20):
        """
        获取一个元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如"id,kw"
        param sec: 等待秒数
        :return: 如果元素可找到则返回element对象，否则返回False
        """
        by, value = self.split_locator(locator)
        try:
            element = WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value))
            return element
        except Exception as e:
            raise e

    def get_elements(self, locator, sec=60):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如"id,kw"
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_elements(by=by, value=value))
            return elements
        except Exception as e:
            raise e

# if __name__ == '__main__':
#     from selenium import webdriver
#     from time import sleep
#     driver = webdriver.Chrome("D:/chromedriver/chromedriver.exe")
#     driver.get('http://192.168.7.131:8081/#/login')
#     driver.maximize_window()
#     a = "css,.user-input > input:nth-child(1)"
#     b = "css,div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
#     c = "css,.el-button"
#     d = "xpath,/html/body/div/section/section/main/div/div/div[1]/button"
#     e = "xpath,//*[@id='app']/section/section/main/div/div[2]/div/form/div[2]/div[2]/div/div/input"
#     # BP1 = Base(driver)
#     bp = Base(driver)
#     p1 = bp.get_element(a).send_keys('admin')
#     p2 = bp.get_element(b).send_keys('admin')
#     p3 = bp.get_element(c).click()
#     sleep(2)
#     p4 = bp.get_element(d).click()
#     p5 = bp.get_element(e).send_keys("C:\\Users\\Administrator\\Desktop\\ODB\\PCADEMODFM_V1.zip")
#     # bp.get_element("plink,地图").click()
#
#     # driver.quit()
