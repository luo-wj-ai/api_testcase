import json
from cloudsystem_test.common.Aurl import baseurl
import requests
from cloudsystem_test.config.存储token值 import write_yamlm
from cloudsystem_test.config.存储现网token值 import write_Vyaml

'''云手机运营管理token值'''
Authorization="bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzQ3ODA5NzQwMTU2Njk0NTI5Iiwib3JpVG9rZW4iOiI0RDlBOTg4MTI3QTc0QkZBQTUxNEZGMTU5NUIxQThFOCIsIm9wZXJhdG9ySWQiOiIxNzQ3ODA5NzQwMTU2Njk0NTI5IiwiYWNjb3VudCI6IjY1MGJlNTcxNzRjNmE2YzE3NjNhODVmYjYwMmI0YTQ1NGVlNTY1MGJjMWY5OTdlYTQ3OWJhODhiNzM4ZWFmM2NkMWNlMTVhNTVjMjI2OGIxMWYiLCJ0ZW5hbnRJZCI6Ijg2MDEiLCJleHAiOjE3MzYyMTEyNzgsImNoYW5uZWwiOiJCTVAifQ.55fSiEWBPkrd0W-GV0wt9Qxv0AqAi8_nraebffvRwzSar8ptSVmr_tlHrijBBEe3b8S3FgGrUBuwDOZQOJwr7A"



'''云手机运营管理接口请求头'''
h = {"Accept": "application/json",
           "Authorization": Authorization,
           "Content-Type": "application/json"
           }


'''获取token值'''
def Token():
    url=baseurl+'/cloudphone/mobile/login'
    upss={
        "mobile": "eK4zDQPGVXunmQxZASHxvDhArq0DJM2to7zyPydJrKicLgrPsducKyGDOZQTpk3L9ffCseC7MH0JRhobQJVNqmzRh9wU0U0YIVT2iBZ598kibhGBfRbb+TjKiJzbqjHrNd56mF0tzKP4N5CrDRr6The8rWf9hUaSy5UEdOE6cvW3/L+soWAm4X3gMLSb3dJjUFV9H0U1AyLyDEh5YINp97iPtX3ZBuJJ79o5oDH1gFwUQ16hyBjEFFG7w7pgGvF2mR7dcbIIc+FU9JhWcmuhzQURWbh8Iv9IRihsKvmIuo/pfYoqcBD0OH4ecOevqutdEalu3wgZraLFhwOAgyEwzw==",
        "password": "iZQvoGTCKViO5+wCLmKVcBUvbAKjN9vxzm7bDKd8pfi1U4Tm1pwQYS6KhEJwFgmreQX3Cq+bDucjOVhPi+bzPel6BxlgCZ5ln9oXKWEpVhNTfjuu4a59I0TJnhuPkz2Br+MccFrpGHqLXNwrfB6fci9WDP7lXsQpa+otAutSQMKkr+NSUByM34fW9YHVQM15uXPM6wyaIVtJdS4pyEIAByF4uGNbdP8Yc0UyJsUw6CxekMNwAkHGBTlupIo/A551+KN9bt5eskejs/B5WCZsBzXSYCy1qecmG9eCHPda3xcS11bjudfxyf61zEa8nP7CGK8iE7efmMDDySF1THp6hg==",
        "et": "1"
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
        "mobile": "Ynu3n60vv8xmlj+P2RkssHmwNnMJIK5QdnN4pXuhz+Otca9Hm7gMasO1vIo7ZP3it36oC4NnoDAkOfXXbdHw5+9TI1VIjEkUvJlRh3/HVDTiUpOdpLiQq5+c4KE1M06kn6gFje1BlS33KxHWXLLf7kN/LsgSpV5Wv0vQeKR+LCdQvoCSZT3gl1yRMQRtJb1gm4shGaAquZYjpLCgk/IzPkgvJ7PuYqVR3dp5JHwvF70wQSIb4RRz0yHkLu0U5MjCsWU2yNsON6cHzFGFmWuFVCeOfIBPt4vazEWLAo+ILmseTFkN2P0n1Gy+D0VSTYEeEJ51c3ULJS/dQXzBJivN+g==",
        "password": "iYkkTPTsgFZhS2OpJQHrJ/QmRu++x9jFQJdW4UIEzJBIYm/FFpYYpPeB4+u6ZURKNm6Gcn20DxIpkBinbogZAR/q/6f7ypm5ST9UHxUhtguh1Tl7phPrA3eoRoUCsxt34Anl2ktUX29T0PhliopZNrfY0rvnfbGci4oLozHH7+Gs4XBqK3eqoxYu46sjVmTWqcgIJ6gNQFeyI/chRYF4zulQPY1MHnZGGIU7SfV8Sp+WnxWz9yJryI5qQuaZxJ8g861/FfBbiA5e+HKZhahUY4cHP8OA1l9eCskVSqltwbBDnERjhchuRDoNA7f/SCCeDBRhTrW1Stw63dMdnz+lgQ==",
        "et": "1"
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
