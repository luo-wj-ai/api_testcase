import os
import  yaml
'''存储平台变量'''
def write_yaml(data):
    with open(os.getcwd()+"/dataweb.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)
    return


def read_yaml(value):
    with open(os.getcwd()+"/dataweb.yaml",encoding="utf-8",mode='r') as f:
        key=yaml.load(f,yaml.FullLoader)
        return key[value]

def clear_yaml():
    with open(os.getcwd()+"/dataweb.yaml",encoding="utf-8",mode='w') as f:
        f.truncate()
    return