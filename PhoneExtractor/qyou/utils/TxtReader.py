'''
@author: Administrator
'''
import abc
import re

class TxtReader:
    __metaclass__ =  abc.ABCMeta
    @abc.abstractmethod
    def read_txt(self): pass
    @staticmethod
    def extract_phone_numbers(txt):
        '''
        130,131,132,133,134,135,136,137,138,139,
        145,147
        150,151,152,153,155,156,157,158,159
        170, 176, 177
        180,182,183,186,187,188,189,
        '''
        p=re.compile(r'(1)(3\d|4[5,7]|5[0-3,5-9]|8[0,2,3,6-9])\D*(\d{4})\D*(\d{4})')
        numbers = [e.group() for e in p.finditer(txt)]
        return numbers



