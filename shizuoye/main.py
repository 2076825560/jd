import unittest
aa=r'C:\Users\86199\Desktop\py\shizuoye\test'
aaa=unittest.defaultTestLoader.discover(aa,pattern='test.py')
ss=unittest.TextTestRunner()
ss.run(aaa)
