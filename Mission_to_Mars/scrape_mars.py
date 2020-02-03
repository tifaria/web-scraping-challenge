
#dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs 

def init_browser():
    executable_path = {'executable_path': 'C:/Users/Tomas Faria/Desktop/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
