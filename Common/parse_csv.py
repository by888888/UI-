import csv, os, pandas
import codecs
from typing import List

from Common.get_project_path import get_project_path


class ParseCsv:
    def __init__(self, file_path, file_name):
        """
        :param file_path: 文件路径
        :param file_name: 文件名
        """
        self.csv_file = os.path.join(get_project_path(), file_path, file_name)

    def parse_specific_csv(self, row):
        """
        :param row: 获取特定行
        :return: 获取数据
        """
        new_list = []
        with open(self.csv_file, 'r', encoding='utf8') as f:
            data = csv.reader(f)
            for i in data:
                new_list.append(i)
            # 删除标题行
            del new_list[0]
        # for j in range(len(new_list)):
        #     return new_list[row][j]
        return new_list[row]

    def parse_any_csv(self):
        """
        :return: 获取任意行
        """
        new_list = []
        with open(self.csv_file, 'r', encoding='utf8') as f:
            data = csv.reader(f)
            for i in data:
                new_list.append(i)
            # 删除标题行
            del new_list[0]
        return new_list


if __name__ == '__main__':
    data = ParseCsv(file_path="Data", file_name="test_003_service_num.csv").parse_any_csv()
    print(len(data))
    print(data)

    # print(data[1])
    # print(data[1])
    # data1 = ParseCsv(file_path="Data", file_name="test_002_task_dfx.csv").parse_any_csv1()
    # print(data1)
    # print(type(data1))
    # print(range(len(data)))
    # for i in range(len(data)):
    #     print(data[i][0])
    # #     print(data[i][1])
    # print(data[0][1])
    #
    # print(data[1][0])
    # print(data[1][1])
