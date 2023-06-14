import os

# 指定目录路径
dir_path = '/content/drive/MyDrive/hl/intvdo'

# 遍历目录下的所有文件
for filename in os.listdir(dir_path):
    # 构造命令字符串
    command = "python run.py --gpu-vendor nvidia -f /content/drive/MyDrive/hl/1.jpg -t /content/drive/MyDrive/hl/intvdo/{} -o /content/drive/MyDrive/hl/out/{}".format(filename, filename)
    # 执行命令
    os.system(command)
