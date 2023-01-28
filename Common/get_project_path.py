import os


def get_project_path():
    file_path = os.path.abspath(__file__)
    project_path = os.path.dirname(os.path.dirname(file_path))
    return project_path


# if __name__ == '__main__':
#     file = get_project_path()
#     print(file)
