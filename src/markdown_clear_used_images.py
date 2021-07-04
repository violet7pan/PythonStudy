import os
import re
import winshell


def clear_used_images(md_path, md_images_dir):
    # 图片文件集合
    imgs = set()
    # Markdown files引用的图片集合
    img_links = set()
    # Markdown file所在目录路径
    md_file_dir = os.path.normpath(md_path) if os.path.isdir(md_path) else os.path.dirname(md_path)
    # print(md_file_dir)
    # 图片目录下的图片文件添加到集合
    for file in os.listdir(md_images_dir):
        imgs.add(file)
    # 编译图片匹配表达式，用于匹配Markdown中的图片URL
    regex = r'/*' + os.path.basename(md_images_dir) + r'/(.*)\)'
    # print("正则表达式:" + regex)
    pattern = re.compile(regex)
    # 遍历Markdown files

    for file in os.listdir(md_file_dir):
        if file.split('.')[-1] == 'md':
            # 打开Markdown file
            md_file = open(os.path.join(md_file_dir, file), 'r', encoding='utf-8')
            # 遍历每一行
            for line in md_file:
                match = pattern.search(line)
                if match:
                    # See: https://www.runoob.com/python/python-reg-expressions.html
                    # group(index)返回匹配字符串元组中索引位置的字符串
                    img_links.add(match.group(1))
    # 永久删除未被引用的图片集合
    # os.remove(imgs - img_links)
    # 删除未被引用的图片到回收站
    for file in imgs - img_links:
        winshell.delete_file(os.path.join(md_images_dir, file))


clear_used_images(r'D:\WorkLib\PyCharm\Study1\Finance\\Inbox.md', r'D:\WorkLib\PyCharm\Study1\Finance\_resources')
