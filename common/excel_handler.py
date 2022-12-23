

import openpyxl

class ExcelMothed:
    def __init__(self,filepath,sheet):
        self.filepath=filepath
        self.sheet=sheet

    def open_excel(self):
        '''打开excel'''
        workbook=openpyxl.load_workbook(self.filepath)
        return workbook
    def get_sheet(self):
        '''获取Sheet表单'''
        workbook=self.open_excel()
        sheet=workbook[self.sheet]
        return sheet
    def get_case(self):
        '''获取所有用例'''
        cell=self.get_sheet()
        rows=list(cell.rows)
        case=[]
        title=[]
        for row in rows[0]:
            title.append(row.value)
        for values in rows[1:]:
            dic={}
            for indx,value in enumerate(values):
                dic[title[indx]]=value.value
            case.append(dic)
        return case
    def excel_write(self,row,column,data):
        '''excel根据单元格位置写入内容'''
        sheet=self.get_sheet()
        sheet.cell(row,column).value=data
        self.excel_save()
        self.excel_close()

    def excel_save(self):
        '''保存excel'''
        self.open_excel().save(self.filepath)

    def excel_close(self):
        '''关闭excel'''
        self.open_excel().close()

