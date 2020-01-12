from log_in import log_in
from bs4 import BeautifulSoup
from selenium import webdriver
import json

if __name__ == '__main__':
    pagen = 2
    page = log_in(pagen)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup)
