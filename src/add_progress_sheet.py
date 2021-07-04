import xlwings

src_wb = xlwings.Book(r'D:\WorkLib\潮州万达基桩数据\A3栋.xlsx')
src_sht = src_wb.sheets['进度表']
dst_wb = xlwings.Book(r'D:\WorkLib\潮州万达基桩数据\A6栋.xlsx')
dst_sht = dst_wb.sheets.add('进度表')

row_num = src_sht.used_range.rows.count
col_num = src_sht.used_range.columns.count
src_data = src_sht.range('A1').expand().formula
dst_sht.range('A1').value = src_data
