import os
import shutil

# 指定目录路径
if not os.path.exists('/content/roop_tmp'):
    os.makedirs('/content/roop_tmp')

src_dir = '/content/drive/MyDrive/hl/intvdo'
dst_dir = '/content/roop_tmp/'
# 确保目标目录存在

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for file_name in os.listdir(src_dir):
    src_file = os.path.join(src_dir, file_name)
    if os.path.isfile(src_file):
        dst_file = os.path.join(dst_dir, file_name)
        shutil.copy(src_file, dst_file)
    
import argparse

# 创建参数解析器
parser = argparse.ArgumentParser(description='Description of your program')

# 添加参数
parser.add_argument('-s', '--src', help='source directory')

# 解析参数
args = parser.parse_args()

# 打印参数
print('Source directory:', args.src)

    
face = args.src
# 遍历目录下的所有文件
for filename in os.listdir(dst_dir):
    # 构造命令字符串
    print("start: python run.py --gpu-vendor nvidia -f '/content/drive/MyDrive/hl/face/{}.jpg' -t '/content/roop_tmp/{}' -o '/content/drive/MyDrive/hl/out/{}-{}".format(face, filename, face, filename))
    command = "python run.py --gpu-vendor nvidia -f '/content/drive/MyDrive/hl/face/{}.jpg' -t '/content/roop_tmp/{}' -o '/content/drive/MyDrive/hl/out/{}-{}'".format(
        face, filename, face, filename)
    # 执行命令
    os.system(command)
