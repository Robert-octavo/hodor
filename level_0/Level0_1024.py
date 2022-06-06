#!/usr/bin/python3
"""https://realpython.com/python-requests/"""
from requests import post
holberton_id = {"id": "4585", "holdthedoor": "submit"}

if __name__ == "__main__":
    for i in range(0, 1024):
        post("http://158.69.76.135/level0.php", data=holberton_id)
