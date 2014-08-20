'''
Created on 2014-08-16 13:05

@author: Administrator
'''
import os

class FileLister(object):
    
    def __init__(self, dirpath):
        self.dirpath = dirpath
    
    def list_files(self, ext=None):
        files = []
        def walk_dir(dirname):
            for root, dirs, filenames in os.walk(dirname):
                for filename in filenames:
                    if self.get_ext(filename) in ext:
                        files.append(os.path.join(root, filename))
                for dirpath in dirs:
                    walk_dir(dirpath)
        walk_dir(self.dirpath)
        return files
    
    @staticmethod
    def get_ext(filepath):
        return filepath.split(".")[-1].lower()


        