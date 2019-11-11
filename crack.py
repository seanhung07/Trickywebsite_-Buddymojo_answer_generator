import requests
from bs4 import BeautifulSoup
import re
import json
id=0
num=1
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
   
    }
choose  = input("\n1. Trickywebsite URL \n2. Buddymojo URL \nEnter:")
if choose==1:
    url  = raw_input("Enter URL: ")
    res=requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    for script in soup.find_all("script"):
        for lines in script.text.split('\n'):
            if('userQuizId' in lines):
                id=int(re.search('\'(.*)\'', lines).group(1))
                print(id)
    url2 = "https://cnb.trickywebsite.com/api/v1/quiz/18?userQuizId="+str(id)+"&type=friend&stats=1"
    response = requests.request("GET", url2, headers=headers)
    code = response.text
    x= json.loads(code)
    for data in x.get("data").get("questions"):
        print('{}. {}'.format(num, data['choosenOption']))
        num+=1
if choose==2:
    url  = raw_input("Enter URL: ")
    res=requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    for script in soup.find_all("script"):
        for lines in script.text.split('\n'):
            if('userQuizId' in lines):
                id=int(re.search('\'(.*)\'', lines).group(1))
                print(id)
    url2 = "https://cn.buddymojo.com/api/v1/quiz/18?userQuizId="+str(id)+"&type=friend&stats=1"
    response = requests.request("GET", url2, headers=headers)
    code = response.text
    x= json.loads(code)
    for data in x.get("data").get("questions"):
        print('{}. {}'.format(num, data['choosenOption']))
        num+=1