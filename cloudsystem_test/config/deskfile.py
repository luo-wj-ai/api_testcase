import os
import  yaml
import random
import string

'''存储订购变量'''
def write_yaml(data):
    with open(os.getcwd()+"/data.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)
    return


def read_yaml(value):
    with open(os.getcwd()+"/data.yaml",encoding="utf-8",mode='r') as f:
        key=yaml.load(f,yaml.FullLoader)
        return key[value]




def clear_yaml():
    with open(os.getcwd()+"/data.yaml",encoding="utf-8",mode='w') as f:
        f.truncate()
    return

def generate_random_string(length=None):
    """
    生成随机字符串，长度在 2 到 10 位之间，字符限制为数字、大小写英文和下划线。

    :param length: 指定字符串长度，如果不指定则随机生成 2 到 10 位的字符串
    :return: 随机字符串
    """
    if length is None:
        length = random.randint(2, 10)  # 随机生成长度
    characters = string.ascii_letters + string.digits  # 包含数字、大小写英文和下划线
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

