import os
import shutil

def split_folder(folder_path, subfolder_count, files_per_subfolder):
    files = os.listdir(folder_path)
    files_count = len(files)
    files_per_subfolder = min(files_per_subfolder, files_count)
    subfolder_count = min(subfolder_count, files_count // files_per_subfolder + 1)
    for i in range(subfolder_count):
        subfolder_path = os.path.join(folder_path, f"{i + 1}")
        os.makedirs(subfolder_path, exist_ok=True)
        start_idx = i * files_per_subfolder
        end_idx = min((i + 1) * files_per_subfolder, files_count)
        for j in range(start_idx, end_idx):
            filename = files[j]
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                if os.path.exists(os.path.join(subfolder_path, filename)):
                    filename, ext = os.path.splitext(filename)
                    filename = f"{filename}_1{ext}"
                shutil.move(file_path, os.path.join(subfolder_path, filename))
    print("文件移动完成！")

def move_files(source_folder, destination_folder):
    files = os.listdir(source_folder)

    for filename in files:
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            if os.path.exists(os.path.join(destination_folder, filename)):
                filename, ext = os.path.splitext(filename)
                filename = f"{filename}_1{ext}"
            shutil.move(file_path, os.path.join(destination_folder, filename))
        elif os.path.isdir(file_path):
            move_files(file_path, destination_folder)

while True:
    print("欢迎使用文件批量移动程序")
    print("请选择功能:")
    print("1. 文件移动到文件夹")
    print("2. 文件夹所有文件移出")
    print("（按下Enter退出）")

    choice = input("请输入选择：")

    if choice == "1":
        folder_path = input("请输入文件夹地址:")
        subfolder_count = int(input("请输入希望将文件分为多少个文件夹:"))
        files_per_subfolder = int(input("请输入每个文件夹应包含的文件数量:"))
        split_folder(folder_path, subfolder_count, files_per_subfolder)
    elif choice == "2":
        source_folder = input("请输入文件夹地址:")
        destination_folder = input("请输入目标文件夹地址:")
        move_files(source_folder, destination_folder)
        print("文件移动完成！")
    else:
        break