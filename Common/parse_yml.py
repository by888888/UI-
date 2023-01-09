import yaml

'''
通过传递文件名、section和key，读取YAML文件中的内容
'''


def parse_yml(file, section, key):
    with open(file, 'r', encoding='utf8') as f:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data[section][key]
