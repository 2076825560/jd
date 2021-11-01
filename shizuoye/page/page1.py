from shizuoye.baes.baes import *
from selenium.webdriver.common.by import By
class page1(baes):
    youhuijuan=(By.XPATH,'//*[@id="navitems-group1"]/li[2]/a')#优惠卷
    sousuo=(By.XPATH,'//*[@id="quan-key"]')#搜索框
    sousuoanjian=(By.XPATH,'//*[@id="search-2014"]/div/button')#搜索按键
    lingqv=(By.XPATH,'//*[@id="61703235"]/div[3]/a')#领取优惠卷
    def zhixing(self):
        self.max()
        sleep(2)
        self.click(self.youhuijuan)
        self.dcq.switch_to.window(self.dcq.window_handles[-1])
        sleep(2)
        self.send_keys(self.sousuo,'水果')
        sleep(2)
        self.click(self.sousuoanjian)
        sleep(2)
        self.click(self.lingqv)




