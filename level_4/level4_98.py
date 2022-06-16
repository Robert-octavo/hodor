#!/usr/bin/python3
"""
https://realpython.com/python-requests/
https://j2logo.com/python/web-scraping-con-python-guia-inicio-beautifulsoup/
install beautifulsoup4 and lxml
python -m pip install beautifulsoup4

http://158.69.76.135/level1.php
when we check the webpage using the explorer
we see that there are anothe inpout in the form with the type of hidden
<input type="hidden" name="key" value="3c2f9655e5bead48..."
we need to get the info from the key to add to our data because
the key value change everytime the form it send

user agent for Windows:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent/Firefox
Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0

"""
import requests
from requests import post, session
from bs4 import BeautifulSoup

holberton_id = {"id": "4585", "holdthedoor": "holdthedoor", "key": ""}
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:10.0) "
            "Gecko/20100101 Firefox/10.0")

header = {
    "User-Agent": user_agent,
    "referer": "http://158.69.76.135/level4.php"
}

url = "http://158.69.76.135/level4.php"

proxy_list = ["'http':  'http://64.227.14.149:80'",
            "'http':  'http://169.57.1.85:8123'",
            "'http':  'http://103.219.194.13:80'",
            "'http':  'http://47.254.39.233:80'",
            "'http':  'http://47.74.18.113:80'",
            "'http':  'http://103.148.72.126:80'",
            "'http':  'http://52.168.34.113:80'",
            "'http':  'http://104.160.189.3:80'",
            "'http':  'http://103.219.194.12:80'",
            "'http':  'http://103.219.194.11:80'",
            "'http':  'http://8.209.210.211:80'",
            "'http':  'http://103.149.162.195:80'",
            "'http':  'http://49.207.36.81:80'",
            "'http':  'http://103.148.72.192:80'",
            "'http':  'http://211.250.133.182:8001'",
            "'http':  'http://3.226.168.144:80'",
            "'http':  'http://159.89.195.14:80'",
            "'http':  'http://117.54.114.102:80'",
            "'http':  'http://202.86.151.82:8888'",
            "'http':  'http://103.81.13.129:60714'",
            "'http':  'http://133.242.237.138:3128'",
            "'http':  'http://20.47.108.204:8888'",
            "'http':  'http://187.217.54.84:80'",
            "'http':  'http://38.55.178.224:80'",
            "'http':  'http://38.55.180.224:80'",
            "'http':  'http://123.63.213.137:80'",
            "'http':  'http://213.230.97.10:3128'",
            "'http':  'http://97.74.92.60:80'",
            "'http':  'http://164.155.150.0:80'",
            "'http':  'http://194.233.73.104:443'",
            "'http':  'http://116.203.214.179:80'",
            "'http':  'http://47.74.0.7:80'",
            "'http':  'http://8.210.83.33:80'",
            "'http':  'http://80.48.119.28:8080'",
            "'http':  'http://66.29.154.103:3128'",
            "'http':  'http://103.232.215.194:80'",
            "'http':  'http://38.55.181.255:80'",
            "'http':  'http://43.250.107.91:80'",
            "'http':  'http://38.55.177.225:80'",
            "'http':  'http://38.55.182.255:80'",
            "'http':  'http://38.55.180.255:80'",
            "'http':  'http://59.15.154.69:13128'",
            "'http':  'http://168.138.211.252:3128'",
            "'http':  'http://36.94.40.123:9812'",
            "'http':  'http://195.158.30.232:3128'",
            "'http':  'http://194.233.73.106:443'",
            "'http':  'http://151.106.18.125:1080'",
            "'http':  'http://129.226.17.43:80'",
            "'http':  'http://121.1.41.162:111'",
            "'http':  'http://64.227.62.123:80'",
            "'http':  'http://51.195.144.68:8888'",
            "'http':  'http://66.94.97.238:443'",
            "'http':  'http://78.154.180.52:81'",
            "'http':  'http://66.29.154.105:3128'",
            "'http':  'http://47.74.152.29:8888'",
            "'http':  'http://185.51.10.19:80'",
            "'http':  'http://146.59.83.187:80'",
            "'http':  'http://67.212.186.102:80'",
            "'http':  'http://67.212.186.100:80'",
            "'http':  'http://67.212.186.101:80'",
            "'http':  'http://85.195.104.71:80'",
            "'http':  'http://43.255.113.232:8082'",
            "'http':  'http://164.155.149.1:80'",
            "'http':  'http://164.155.147.31:80'",
            "'http':  'http://164.155.145.31:80'",
            "'http':  'http://164.155.146.31:80'",
            "'http':  'http://164.155.150.1:80'",
            "'http':  'http://164.155.148.1:80'",
            "'http':  'http://67.212.186.99:80'",
            "'http':  'http://164.155.147.0:80'",
            "'http':  'http://164.155.149.0:80'",
            "'http':  'http://188.0.147.102:3128'",
            "'http':  'http://159.203.61.169:3128'",
            "'http':  'http://38.55.182.225:80'",
            "'http':  'http://38.55.183.224:80'",
            "'http':  'http://164.155.148.0:80'",
            "'http':  'http://164.155.146.0:80'",
            "'http':  'http://194.233.73.105:443'",
            "'http':  'http://193.140.143.67:80'",
            "'http':  'http://194.233.69.90:443'",
            "'http':  'http://162.144.116.103:80'",
            "'http':  'http://117.54.114.96:80'",
            "'http':  'http://142.44.148.56:8080'",
            "'http':  'http://164.155.150.31:80'",
            "'http':  'http://110.170.126.13:3128'",
            "'http':  'http://164.155.145.0:80'",
            "'http':  'http://38.55.180.225:80'",
            "'http':  'http://216.137.184.253:80'",
            "'http':  'http://161.97.158.118:1081'",
            "'http':  'http://66.196.238.179:3128'",
            "'http':  'http://151.106.18.122:1080'",
            "'http':  'http://195.123.245.120:80'",
            "'http':  'http://116.254.116.99:8080'",
            "'http':  'http://194.233.69.38:443'",
            "'http':  'http://213.230.69.193:3128'",
            "'http':  'http://194.233.69.41:443'",
            "'http':  'http://95.59.26.129:80'",
            "'http':  'http://151.106.17.126:1080'",
            "'http':  'http://212.46.230.102:6969'",
            "'http':  'http://154.236.177.101:1981'",
            ]


success = 'Hold the Door challenge - Level 4'
if __name__ == "__main__":
    for i, proxy in enumerate(proxy_list):
        print(proxy)
        """print(i)"""
        try:
            session = requests.session()
            session.proxies = {
                'http': 'http://10.10.10.10:8000',
                'https': 'http://10.10.10.10:8000',
            }
            web = session.get(url)
            soup = BeautifulSoup(web.text, "html.parser")
            hidden_key = soup.find("form", {"method": "post"})
            hidden_key = hidden_key.find("input", {"type": "hidden"})
            """print(hidden_key["value"])"""
            holberton_id["key"] = hidden_key["value"]
            print(holberton_id)
            check = session.post(url, data=holberton_id, timeout=5)
            print(check.text)
            if check.status_code == 200 and success in check.text:
                print("ok!")
        except Exception as e:
            print("fail")
            print(check.status_code)
            print(check.text)
