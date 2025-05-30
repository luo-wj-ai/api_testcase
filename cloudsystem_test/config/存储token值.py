import os
import yaml
'''存储云手机token变量'''
def write_yamlm(data):
    with open(os.getcwd()+"/datatoken.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)


def read_yamlm(value):
    with open(os.getcwd()+"/datatoken.yaml",encoding="utf-8",mode='r') as f:
        key=yaml.load(f,yaml.FullLoader)
        return key[value]

def clear_yamlm():
    with open(os.getcwd()+"/datatoken.yaml",encoding="utf-8",mode='w') as f:
        f.truncate()


# if __name__ == '__main__':
#     a=read_yamlm("token")
#     print(a)


"""new——存储测试后台的登录token变量"""
def write_backendyamlm(data):
    with open(os.getcwd()+"/test_data/Test_backend_Token.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)


def read_backendyamlm(value):
    with open(os.getcwd()+"/test_data/Test_backend_Token.yaml",encoding="utf-8",mode='r') as f:
        key=yaml.load(f,yaml.FullLoader)
        return key[value]

def clear_backendyamlm():
    with open(os.getcwd()+"/test_data/Test_backend_Token.yaml",encoding="utf-8",mode='w') as f:
        f.truncate()