import xlrd
import xlwt
from xlrd import xldate_as_tuple
from datetime import datetime

print("hello")


def process_oa():
    workbook = xlrd.open_workbook('test.xlsx')
    sheet = workbook.sheet_by_index(0)

    for row_index in range(sheet.nrows):
        row = sheet.row_values(row_index)
        cell = sheet.cell(row_index, 2)
        cell_value = sheet.cell_value(row_index, 2)
        if cell.ctype == 3:
            year, month, day, hour, minute, second = xldate_as_tuple(cell_value, 0)

            print(hour)


if __name__ == '__main__':
    process_oa()
