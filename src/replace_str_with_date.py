import xlwings
import datetime


class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value


pile = _const()
pile.col_date = 'C'
pile.col_len_pile_1 = 'H'
pile.col_len_pile_2 = 'L'
pile.col_len_pile_3 = 'P'
pile.col_len_pile_4 = 'T'
pile.col_final_pressure = 'AA'
pile.col_depth_top_to_ground = 'AX'
pile.col_depth_bottom_to_ground = 'AY'

wb = xlwings.Book(r'D:\SyncLib\NutstoreSync\Document\PileFoundation\万达广场\基桩施工数据\A6栋.xlsx')
sht = wb.sheets['施工记录']
row_num = sht.used_range.rows.count
col_num = sht.used_range.columns.count

# print(sht.range('C' + '14').value)
# print(type(sht.range('C' + '14').value))

for i in range(13, row_num + 1, 29):
    for j in range(i, i+15):
        cell = sht.range('C' + j.__str__()).value
        if isinstance(cell, str):
            print(datetime.datetime.strptime(cell, '%Y.%m.%d'))
            sht.range(pile.col_date + j.__str__()).value = datetime.datetime.strptime(cell, '%Y.%m.%d')
            pass

# print(isinstance(sht.range('C2028').value, datetime.datetime))
# print(type(sht.range('C2028').value))
