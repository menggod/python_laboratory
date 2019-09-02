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
        date_time = sheet.cell(row_index, 0)
        time_out = sheet.cell(row_index, 2)


        print(date_time)

        for column_index in range(len(sheet.row_values(0))):
            # cell = sheet.cell(row_index, column_index)
            pass

    # xldate_as_tuple(cell, 0)

    # for row_num in range(1, nrows):
    #     row_values = sheet.row_values(row_num)
    #     if row_values:
    #         str_obj = {}
    #     for i in range(len(first_row_values)):
    #         ctype = sheet.cell(num, i).ctype
    #         cell = sheet.cell_value(num, i)
    #         print(cell)
    #         if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
    #             cell = int(cell)  # 浮点转成整型
    #             cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
    #         elif ctype == 3:
    #             date = datetime(*xldate_as_tuple(cell, 0))
    #             cell = date.strftime('%H:%M:%S')
    #         elif ctype == 4:
    #             cell = True if cell == 1 else False
    #         str_obj[first_row_values[i]] = cell
    #     list.append(str_obj)
    #     num = num + 1

    print("end")


if __name__ == '__main__':
    process_oa()
