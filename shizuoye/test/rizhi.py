import logging
class Log():
    def __init__(self,fname):
        self.fname=fname
    def LOG(self):
        logg=logging.getLogger()
        logg.setLevel(0)
        frozenset=logging.Formatter(
            '%(name)s--%(asctime)s--%(levelno)s--%(levelname)s--%(message)s'
        )
        fn=logging.FileHandler(self.fname,mode='w',encoding='utf-8')
        fn.setFormatter(frozenset)
        logg.addHandler(fn)