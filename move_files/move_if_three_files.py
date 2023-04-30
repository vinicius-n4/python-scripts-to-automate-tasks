import os
import shutil


root_dir = r'C:\path\to\files'
dst_dir = r'C:\path\to\multi_files'

index = 0
for src_dir, dirs, _ in os.walk(root_dir):
    for d in dirs:
        files = os.listdir(os.path.join(root_dir, d))

        if len(files) < 3:
            continue
        else:
            multi_images = os.listdir(os.path.join(root_dir, d))

            for f in multi_images:
                index += 1
                src_file = os.path.join(root_dir, d, f)
                dst_file = os.path.join(dst_dir, d, f)
                if not os.path.exists(os.path.join(dst_dir, d)):
                    os.makedirs(os.path.join(dst_dir, d))

                print("[%s] - Copying file from [%s] to [%s] ..." % (index, src_file, dst_file))
                shutil.copy2(src_file, dst_file)
