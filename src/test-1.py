from datetime import datetime

# a = [1,2,3,4]
for i in range(1, 366 + 1):
    for j in range(1, 6 + 1):
        print(chr(ord('A') + j - 1) + str(i))
        # dst_sht.range(chr(ord('A') + j - 1) + str(i)).value = src_sht.range(chr(ord('A') + j - 1)).formula