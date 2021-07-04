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
write_data = xlutils.copy.copy(wb)
write_save = write_data.get_sheet(0)
write_save.write(13, CONST.INDEX_DATE)
write_data.save('123.xls')