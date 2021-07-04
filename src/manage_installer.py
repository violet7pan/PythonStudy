import os
import shutil
import glob


DIRECTORIES = {
    "图片": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
           ".heif", ".psd"],
    "视频": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
           ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "文档": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
           ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
           ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
           "pptx", ".csv", ",pdf"],
    "压缩文件": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
             ".dmg", ".rar", ".xar", ".zip"],
    "影音": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
           ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "文本": [".txt", ".in", ".out"],
    "编程": [".py", ".html5", ".html", ".htm", ".xhtml", ".c", ".cpp", ".java", ".css"],
    "可执行程序": [".exe"],
    'Windows软件': ['.exe', '.msixbundle']
}


def manage_pcsoft(input_dir, output_dir, recursively=False):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        for file in glob.glob(f'{input_dir}/**', recursive=recursively):
            if os.path.isfile(file):
                filename = os.path.basename(file)
                if '.' in filename:
                    suffix = file.split('.')[-1]
                    if '.' + suffix in DIRECTORIES['Windows软件']:
                        shutil.move(file, f'{output_dir}')
                        # shutil.copy(file, f'{output_dir}')


manage_pcsoft(r'F:\DownloadLib\IDM', r'F:\DownloadLib\PCSoft')
