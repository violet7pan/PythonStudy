import xlrd
import xlutils.copy
import xlwt


def constant(f):
    def f_set(self, value):
        raise TypeError

    def f_get(self):
        return f()

    return property(f_get, f_set)


class _Const(object):
    @constant
    def INDEX_DATE():
        return 2

    @constant
    def INDEX_LEN_PILE_SECTION_1():
        return 7

    @constant
    def INDEX_LEN_PILE_SECTION_2():
        return 11

    @constant
    def INDEX_LEN_PILE_SECTION_3():
        return 15

    @constant
    def INDEX_LEN_PILE_SECTION_4():
        return 19

    @constant
    def INDEX_FINAL_PRESSURE():
        return 26

    @constant
    def INDEX_TIME_PRESSURE():
        return 28

    @constant
    def INDEX_DEPTH_PILE_TIP_TO_GROUND():
        return 49

    @constant
    def INDEX_DEPTH_PILE():
        return 50


CONST = _Const()
# 读文件
wb = xlrd.open_workbook('D:/WorkLib/PyCharm/A3Copy.xls', formatting_info=True)
wb2 = xlutils.copy.copy(wb)

table = wb.sheet_by_name("施工记录")
row_num = table.nrows
col_num = table.ncols
# lists = [str(table.cell_value(i, CONST.INDEX_DEPTH_PILE)) for i in range(12, 27)]
# print(lists)

# print(table.cell_type(12, CONST.INDEX_DATE))
# print(table.cell_value(12, CONST.INDEX_DATE))


date_format = xlwt.XFStyle()
date_format.num_format_str = 'yyyy/mm/dd'
table2 = wb2.get_sheet(0)
date = table.cell_type(12, CONST.INDEX_DATE)
if table.cell_type(13, CONST.INDEX_DATE) == xlrd.biffh.XL_CELL_DATE:
    print(xlrd.xldate.xldate_as_datetime(table.cell_value(12, CONST.INDEX_DATE), wb.datemode))
elif table.cell_type(13, CONST.INDEX_DATE) != xlrd.biffh.XL_CELL_DATE:
    print(table.cell_type(13, CONST.INDEX_DATE))
    date = table.cell_value(13, CONST.INDEX_DATE)
    print(date)
    table2.write(13, CONST.INDEX_DATE, date, date_format)
    wb2.save('date_format.xls')
