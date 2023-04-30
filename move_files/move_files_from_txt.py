import os
import shutil


root_src_dir = r'C:\path\to\files'
root_dst_dir = r'C:\path\to\output\files'

index = 0
with open("folders.txt", "r") as file:
    folders = file.readlines()
for folder in folders:

    folder = folder.replace("\n", "")

    for src_dir, dirs, _ in os.walk(root_src_dir):
        for dir in dirs:
            if folder == dir:
                files = os.listdir(os.path.join(root_src_dir, dir))

                for file in files:
                    index += 1
                    src_file = os.path.join(root_src_dir, dir,  file)
                    dst_file = os.path.join(root_dst_dir, file)

                    print("[%s] - Copying file from [%s] to [%s] ..." % (index, src_file, dst_file))
                    # shutil.move(src_file, dst_file)
                    shutil.copy(src_file, dst_file)
