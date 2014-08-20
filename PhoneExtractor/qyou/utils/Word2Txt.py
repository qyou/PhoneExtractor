#-*- coding: GBK -*-
'''

@author: qyou@nlpr.ia.ac.cn
'''

import win32com.client
from TxtReader import TxtReader

class Word2Txt(TxtReader):
    '''
    Extract MS Office Word to Txt content
    '''


    def __init__(self, filepath):
        '''
        save word file path to the class field `filepath`
        '''
        self.filepath = filepath
    
    
    def read_txt(self):
        app = win32com.client.Dispatch('Word.Application')
        doc = app.Documents.Open(self.filepath)
        txt = doc.Content.Text
        app.Quit()
        return txt
        