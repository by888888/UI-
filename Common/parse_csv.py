import csv


def parse_csv(file):
    new_list = []
    with open(file, 'r', encoding='utf8') as f:
        data = csv.reader(f)
        for i in data:
            new_list.append(i)
        # 删除标题行
        del new_list[0]
    return new_list
