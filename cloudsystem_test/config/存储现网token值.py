import os
import yaml

def write_Vyaml(data):
    with open(os.getcwd()+"/datatoken2.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)


def read_Vyaml(value):
    with open(os.getcwd()+"/datatoken2.yaml",encoding="utf-8",mode='r') as f:
        key=yaml.load(f,yaml.FullLoader)
        return key[value]


def clear_Vyaml():
    with open(os.getcwd()+"/datatoken2.yaml",encoding="utf-8",mode='w') as f:
        f.truncate()
