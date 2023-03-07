import yaml
import os
from Common.get_project_path import get_project_path

'''
通过传递文件名、section和key，读取YAML文件中的内容
'''


class ParseYml():

    def __init__(self, file_path, file_name):
        self.yam_file = os.path.join(get_project_path(), file_path, file_name)

    # def parse_yml(self, section, key):
    #     with open(self.yam_file, 'r', encoding='utf8') as f:
    #         data = yaml.load(f, Loader=yaml.FullLoader)
    #         return data[section][key]

    def parse_yml(self,section):

        with open(self.yam_file, 'r', encoding='utf8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data[section]


if __name__ == '__main__':
    value = ParseYml(file_path="Config", file_name="element.yml").parse_yml('login')
    # value = parse_yml1('../Config/redmine.yml', 'website', 'host')
    print(value['username'])

