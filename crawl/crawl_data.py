from selenium import webdriver
import pandas as pd
from dataprocess.process import DataProcess
from types import TracebackType

class CrawlData(webdriver.Chrome):
    def __init__(self,teardown=True):
        super(CrawlData,self).__init__()
        self.teardown = teardown
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.teardown:
            self.quit()

    def land_page(self,url:str):
        self.get(url)











# driver = webdriver.Firefox()
# driver.get("https://www.ikea.com/sa/en/p/aepplaroe-drop-leaf-table-outdoor-brown-stained-brown-40208531/")
# driver.implicitly_wait(8)
# get_url = driver.current_url
# print("The current url is:"+str(get_url))