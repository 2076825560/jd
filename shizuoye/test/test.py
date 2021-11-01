from shizuoye.page.page import *
from shizuoye.page.page1 import *
from shizuoye.page.page2 import *
from shizuoye.test.rizhi import Log
import logging
log1=Log('logg.log')
log1.LOG()
import unittest
class test(unittest.TestCase):
    def setUp(self) -> None:
        self.dcq = webdriver.Chrome(r"C:\Users\86199\Desktop\chromedriver.exe")
        self.dcq.get('https://www.jd.com/')

    @classmethod
    def setUpClass(cls) -> None:
        pass
    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test01(self):
        logging.info('开始')
        page(self.dcq).zhixing()
        print(self.dcq.title)
        logging.debug('结束')
        self.assertEqual('QQ帐号安全登录',self.dcq.title)

    def test02(self):
        logging.error('开始')
        page1(self.dcq).zhixing()
        print(self.dcq.title)
        logging.warning('结束')
        self.assertIsNot('搜索结果 - 领券中心',self.dcq.title)
    def test03(self):
        logging.error('开始')
        page2(self.dcq).zhixing()
        print(self.dcq.current_url)
        logging.warning('结束')
        self.assertNotIn('https://search.jd.com/Search?keyword=%E6%B0%B4%E6%9E%9C&enc=utf-8&wq=%E6%B0%B4%E6%9E%9C&pvid=62da17c9af734761bf0628294a41d6e3',self.dcq.current_url)
if __name__ == '__main__':
    unittest.main()
#     suite=unittest.TestSuite()
#     suite.addTest(test('test01'))
#     runn=unittest.TextTestRunner()
#     runn.run(suite)
