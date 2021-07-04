import os


def get_filelist(directory):
    filelist = open('filelist.txt', 'w+', encoding='utf-8')
    dirlist = open('dir.txt', 'w+', encoding='utf-8')
    d_ctr = 1
    f_ctr = 1
    for root, dirs, files in os.walk(directory):
        # 文件夹列表
        for d in dirs:
            # print(dir)
            dirlist.write(str(d) + '---' + d)
            dirlist.write('\n')
            d_ctr += 1
        # 文件列表
        for filename in files:
            # 拼接全路径
            fullname = os.path.join(root, filename)
            filelist.write(str(f_ctr) + '---' + fullname)
            filelist.write('\n')
            f_ctr += 1
    dirlist.close()
    filelist.close()


if __name__ == "__main__":
    get_filelist(r'D:\WorkLib\PyCharm\PythonStudy')
