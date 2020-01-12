import requests
import time

# simulative logging in
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = { 'User-Agent' : user_agent }

def log_in():
    url = input()
    page = requests.get(url = url, headers = headers)
    return page

def log_in2(url):
    page = requests.get(url = url, headers = headers)
    return page
