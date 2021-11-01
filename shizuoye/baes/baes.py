from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class baes():
    def __init__(self,dcq):
        self.dcq=dcq
    def url(self,url):
        self.dcq.get(url)
    def click(self,str):
        self.dcq.find_element(*str).click()
    def send_keys(self,str,txt):
        self.dcq.find_element(*str).send_keys(txt)
    def max(self):
        self.dcq.maximize_window()
    def dengdai(self,str):
        aa=self.dcq.find_element(*str)
        ActionChains(self.dcq).click(aa).perform()

    def shanchu(self,str):
        self.dcq.find_element(*str).send_keys(Keys.BACK_SPACE)
    def enter(self,str):
        self.dcq.find_element(*str).send_keys(Keys.ENTER)




