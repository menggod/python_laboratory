import random

import xlrd
import xlwt
from xlrd import xldate_as_tuple
from datetime import datetime, timedelta


def process_oa():
    workbook = xlrd.open_workbook('test.xlsx')
    sheet = workbook.sheet_by_index(0)

    all_list = []

    for row_index in range(sheet.nrows):
        lis = []
        cell = sheet.cell(row_index, 2)
        cell_value = sheet.cell_value(row_index, 2)

        if cell.ctype == 3:
            year, month, day, hour, minute, second = xldate_as_tuple(cell_value, 0)

            new_date = "%d:%d:%d" % (hour, minute, second)
            date_time = datetime.strptime(new_date, "%H:%M:%S")

            base_time = datetime(1900, 1, 1, 21, 0, 0)
            if date_time >= base_time:
                minute_int = random.randint(2, 6)
                second_int = random.randint(8, 60)
                date_time = date_time + timedelta(minutes=minute_int, seconds=second_int)
                # print(date_time, minute_int, second_int)

                lis.append(sheet.cell_value(row_index, 0))
                lis.append(date_time.strftime("%H:%M:%S"))
                lis.append(random.randint(89, 93))
                all_list.append(lis)
            else:
                pass
    print(all_list)
    write_xls(all_list)


datastyle = xlwt.XFStyle()
datastyle.num_format_str = 'HH:mm-ss'


def write_xls(all_list):
    count = 0
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=True)

    for each in range(0, len(all_list)):
        values = all_list[each]
        for value_index in range(0, len(values)):
            sheet.write(count, value_index, values[value_index])
        count = count + 1
    book.save('oa_test.xlsx')


if __name__ == '__main__':
    process_oa()
