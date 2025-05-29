import json
from cloudsystem_test.common.Aurl import baseurl
import requests
from cloudsystem_test.config.存储token值 import write_yamlm, write_backendyamlm, clear_backendyamlm, read_backendyamlm
from cloudsystem_test.config.存储现网token值 import write_Vyaml


"""获取luo测试后台的token值"""
def Get_Authorization():
    url = "https://koophone-cc.cmtest.xyz:8080/portal/system/admin/v1/login"
    headers={
        'X-Deviceinfo': '4g||web|5.4.1|||Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36|17211872105829HGM6PelMy||Windows 10|1920X1080|zh||||||',
        'Content-Type': 'application/json'
    }
    upss = {
        "loginAccount": "luoweijie",
        "password": "Luoweijie:123",
        "verificateKey": "lzSNkXaTHZFss-Oa8dfK0"
   }
    res = requests.post(url=url, json=upss, headers=headers)
    result=json.loads(res.text)
    atoken=result["data"]["data"]["token"]["accessToken"]
    datas = {"token": atoken}
    clear_backendyamlm()
    write_backendyamlm(datas)
    return "bearer "+ str(atoken)

"""上一个人这样写h，我没办法，方法都耦住了，写这个是无奈之举，为了每次在运行的时候更新token，但是又不想每次用h的时候都更新token,上一个人的h还是写死的，只是变量，我真的套了"""
'''云手机运营管理接口请求头'''
def h(update=False):
    if update==True:
        Get_Authorization()
    return {"Accept": "application/json",
           "Authorization": read_backendyamlm("token"),
           "Content-Type": "application/json"
           }

'''云手机运营管理token值'''

'''获取token值'''
def Token():
    baseurl="https://koophone-cc.cmtest.xyz"
    url=baseurl+'/cloudphone/mobile/login'
    upss={
    "mobile": "MTgsix2+2XiQD0JbjWits4RyL1Y8AEfXM+2ZGFC1wEJ9IeNPQU1Dhv/mJteQzqC3OlFwwqfriE5F2A0juDYCeLdpy7xv6kJl1+nH4SwQ3F4Rfxslxrr0n9dF5lgRIgBJcI0Lnb8Nle0kfLRAbo+0iWj8pKXOeBee9Zk3H5YrKo4TszielpueeRozrtwSKz6qxxJoCNtxLwM/Q65DAsupfvNAXoyHG6WZhH8ctOS/C+UB1UVqmrgb4ZDl7iZ/gDc/KIHsaLe/3oIa9w8d+pCfSxHRwwDt9taDFMglSCN2ejNIdoHZTmP7BUO7+Lb46CVVb6fRxB0QPeg4eBrVH6cmvw==",
    "password": "NNNWCrt/rFiVpYOaGC+XcGeQb5WE4T6P5wENAuI5e86rk2h+Bu5Im1TRXw9/qfiFWoA7qC90xkZMc9Qw65h293SjI4lWKFC5DJGqA0B0Yn9tO1wQvwcWu5J7zrI1Eqh8QYbabRTFNQEn5UqG0qYw7Ag1rl4eeFfKxZ56G2gZ5j8BQJEUCFRLSj2l9F7JCaytdPetHOkWscjcn9sK8AOarCoFy8fdBV6UcbV5ZyMNtF1ogCxYZJvfZDXc0aGWKDK2sp3hBvFk3LuD+zKErfeiOXdT4MfaNYrKQvtJcwM4z2DcpGgjB5XvTX//PhFUA7R/c5BxTRdZTzZbhILGtANgFg=="
}
    headers = {
    # 'X-Deviceinfo': '4g||web|3.20|||Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0|1702361160685D3S4BKYOk||windows 10|1920X1080|zh||||||',
        'X-Deviceinfo':  '4g||web|5.4.1|||Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36|17211872105829HGM6PelMy||Windows 10|1920X1080|zh||||||',
    'Content-Type': 'application/json'
    }
    res=requests.post(url=url,json=upss,headers=headers)
    # print(res.text)
    result=res.text
    result=json.loads(result)
    atoken=result["data"]["accessToken"]
    datas={"token":atoken}
    write_yamlm(datas)
    return atoken


'''获取token值(现网环境token)'''
def Token2():
    url='https://cpability.buy.139.com/cloudphone/mobile/login'
    upss={
        "mobile": "MTgsix2+2XiQD0JbjWits4RyL1Y8AEfXM+2ZGFC1wEJ9IeNPQU1Dhv/mJteQzqC3OlFwwqfriE5F2A0juDYCeLdpy7xv6kJl1+nH4SwQ3F4Rfxslxrr0n9dF5lgRIgBJcI0Lnb8Nle0kfLRAbo+0iWj8pKXOeBee9Zk3H5YrKo4TszielpueeRozrtwSKz6qxxJoCNtxLwM/Q65DAsupfvNAXoyHG6WZhH8ctOS/C+UB1UVqmrgb4ZDl7iZ/gDc/KIHsaLe/3oIa9w8d+pCfSxHRwwDt9taDFMglSCN2ejNIdoHZTmP7BUO7+Lb46CVVb6fRxB0QPeg4eBrVH6cmvw==",
        "password": "NNNWCrt/rFiVpYOaGC+XcGeQb5WE4T6P5wENAuI5e86rk2h+Bu5Im1TRXw9/qfiFWoA7qC90xkZMc9Qw65h293SjI4lWKFC5DJGqA0B0Yn9tO1wQvwcWu5J7zrI1Eqh8QYbabRTFNQEn5UqG0qYw7Ag1rl4eeFfKxZ56G2gZ5j8BQJEUCFRLSj2l9F7JCaytdPetHOkWscjcn9sK8AOarCoFy8fdBV6UcbV5ZyMNtF1ogCxYZJvfZDXc0aGWKDK2sp3hBvFk3LuD+zKErfeiOXdT4MfaNYrKQvtJcwM4z2DcpGgjB5XvTX//PhFUA7R/c5BxTRdZTzZbhILGtANgFg==",
    }
    headers = {
    # 'X-Deviceinfo': '4g||h5|3.1|||Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/115.0.0.0|1660336099700z4HVwnzmBn||windows 10|390X844|zh||||02090||',
    'X-Deviceinfo': '4g||web|5.4.1|||Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36|17211872105829HGM6PelMy||Windows 10|1920X1080|zh||||||',
    'Content-Type': 'application/json'
    }
    res=requests.post(url=url,json=upss,headers=headers)
    # print(res.text)
    result=res.text
    result=json.loads(result)
    atoken=result["data"]["accessToken"]
    datas={"tokenn":atoken}
    write_Vyaml(datas)
    return atoken

if __name__ == '__main__':
    print(Get_Authorization())

