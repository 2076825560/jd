from shizuoye.baes.baes import *
from selenium.webdriver.common.by import By
class page2(baes):
    suo=(By.XPATH,'//*[@id="key"]')#搜索
    suodian=(By.CLASS_NAME,'button')#搜索按键
    jiaru=(By.XPATH,'//*[@id="J_goodsList"]/ul/li[1]/div/div[7]/a[3]')#加入购物A车
    def zhixing(self):
        self.max()
        self.send_keys(self.suo,'水果')
        sleep(2)
        self.click(self.suodian)
        sleep(2)
        self.dcq.execute_script('window.scrollTo(0,500)')
        sleep(5)
        self.click(self.jiaru)