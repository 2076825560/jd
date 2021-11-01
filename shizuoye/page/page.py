from shizuoye.baes.baes import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class page(baes):
    nihao=(By.CLASS_NAME,'link-login')#请登录
    qq=(By.CLASS_NAME,'QQ-icon')#qq登录
    zhanghaomimadenglu=(By.ID,'switcher_plogin')#账号密码登录
    zhanghao=(By.NAME,'u')#帐号
    mima=(By.NAME,'p')#密码
    shouquan=(By.XPATH,'//*[@id="login_button"]')#授权并登录
    def zhixing(self):
        self.max()
        sleep(1)
        WebDriverWait(self.dcq,10,0.5).until(EC.presence_of_element_located((self.nihao))).click()
        sleep(2)
        self.dengdai(self.qq)
        self.dcq.implicitly_wait(5)
        self.dcq.switch_to.frame('ptlogin_iframe')
        self.click(self.zhanghaomimadenglu)
        sleep(2)
        self.send_keys(self.zhanghao,'2063527051')
        sleep(2)
        self.send_keys(self.mima,'dcq210116210116')
        sleep(2)
        self.click(self.shouquan)