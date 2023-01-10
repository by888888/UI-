import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./Report/report -o ./Report/allure_report --clean")
