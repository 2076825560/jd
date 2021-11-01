import unittest
from BeautifulReport import BeautifulReport
bao=unittest.defaultTestLoader.discover('.','test.py')
gao=BeautifulReport(bao)
gao.report('.','baogao.html')