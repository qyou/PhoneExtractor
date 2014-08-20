'''
@author: qyou@nlpr.ia.ac.cn
'''
import win32com.client
from TxtReader import TxtReader

class Excel2Txt(TxtReader):
    def __init__(self, filepath):
        self.filepath = filepath
    
    def read_txt(self):
        txt = ''
        app = win32com.client.Dispatch('Excel.Application')
        workbook = app.Workbooks.Open(self.filepath)
        worksheets = workbook.Worksheets
        for worksheet in worksheets:
            nrows = worksheet.UsedRange.Rows.Count
            ncolumns = worksheet.UsedRange.Columns.Count
            for i in range(nrows):
                rows = []
                for j in range(ncolumns):                    
                    v =  worksheet.Cells(i+1,j+1).Value
                    if v is None:
                        rows.append(" ")
                    else:
                        rows.append(str(v))
                txt += ', '.join(rows)
                txt += "\n"
            txt += "--------------------------------\n"  
        app.Quit()                      
        return txt