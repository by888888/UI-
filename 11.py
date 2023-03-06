# 1.导包 unittest/parameterized
import json
import unittest
from parameterized import parameterized


# 组织测试数据[(),(),()]or[[],[],[]]
# "desc":"正确的用户名和密码",
# "username":"admin",
# "password":"123456",
# "expect":"登录成功"
def build_data():
    with open('data.json', encoding="utf-8") as f:
        result = json.load(f)  # [{},{},{}]
        data = []
        for i in result:  # i {}
            data.append((i.get("expect"), i.get('username'), i.get("password")))
    return data


print(build_data())
print(type(build_data()))

# 2.定义测试类
# class TestLogin(unittest.TestCase):
#     # 3.书写测试方法(用到的测试数据使用变量代替)
#     @parameterized.expand(build_data())
#     def test_login(self,expect,username,password):
#         self.assertEqual(expect,login(username,password))

# 4.组织测试数据并传参(装饰器@)

if __name__ == "__main__":
    unittest.main()
