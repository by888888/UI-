# 公用的封装方法

class publicmethod:
    def __init__(self, driver):
        self.driver = driver

    # 拉直最底部
    def scrollheight(self,):
        ele = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        return ele
