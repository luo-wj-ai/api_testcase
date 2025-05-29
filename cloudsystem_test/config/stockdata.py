# import os
# import  yaml
# '''存储请求参数数据'''
# file_path= '../test_data/data.yaml'
# def write_cyaml(data):
#     with open(file_path,encoding="utf-8",mode="a+") as f:
#         yaml.dump(data,stream=f,allow_unicode=True)
#     return
#
# def read_cyaml(value):
#     with open(file_path,encoding="utf-8",mode='r') as f:
#         key=yaml.load(f,yaml.FullLoader)
#         return key[value]
#
# def clear_cyaml():
#     with open(file_path,encoding="utf-8",mode='w') as f:
#         f.truncate()
#     return

import os
import yaml

'''存储请求参数数据'''
def get_file_path():
    return os.path.join(os.getcwd(), "test_data", "data.yaml")

def write_cyaml(data):
    file_path = get_file_path()
    with open(file_path, encoding="utf-8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)
    return

def read_cyaml(value):
    file_path = get_file_path()
    with open(file_path, encoding="utf-8", mode='r') as f:
        key = yaml.load(f, yaml.FullLoader)
        return key[value]

def clear_cyaml():
    file_path = get_file_path()
    with open(file_path, encoding="utf-8", mode='w') as f:
        f.truncate()