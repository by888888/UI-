import os
import pytest, allure
from Common.get_project_path import get_project_path

test_path = os.path.join(get_project_path(), "Test", "TestCase")
allure_report = os.path.join(get_project_path(), "Report", "allure_report")
print(test_path)
#
if __name__ == '__main__':
    pytest.main([test_path, "-sv", "--alluredir", allure_report])
    os.system("allure generate {} -o ./report/html --clean".format(allure_report))
