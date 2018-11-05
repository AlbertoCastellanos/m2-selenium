from bs4 import BeautifulSoup
from selenium import webdriver

def getPage(url):
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    return soup













# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'