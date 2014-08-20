#-*- coding: GBK -*-
'''

@author: qyou@nlpr.ia.ac.cn
'''


from utils import Word2Txt
from utils import Excel2Txt
from utils import FileLister
import os
import sys

def usage():
    pass

def main():
    argc = len(sys.argv)
    if argc < 2:
        usage()
    else:
        numbers = []
        def get_numbers(filepath):
            numbers = []
            if FileLister.FileLister.get_ext(filepath) in ['xls', 'xlsx']:
                excel = Excel2Txt.Excel2Txt(filepath)
                txt = excel.read_txt()
                numbers = excel.extract_phone_numbers(txt)
            elif FileLister.FileLister.get_ext(filepath) in ['doc', 'docx']:
                word = Word2Txt.Word2Txt(filepath)
                txt = word.read_txt()
                numbers = word.extract_phone_numbers(txt)
            else:
                print "Unsupported files"
            return numbers
        if os.path.isdir(sys.argv[1]):
            filelister = FileLister.FileLister(sys.argv[1])
            filepaths = filelister.list_files(ext=['xls', 'xlsx', 'doc', 'docx'])
            for filepath in filepaths:
                numbers += get_numbers(filepath)
        else:
            numbers += get_numbers(filepath)
        print numbers  

if __name__ == '__main__':
    main()