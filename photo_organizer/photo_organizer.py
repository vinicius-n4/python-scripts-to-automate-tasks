import argparse
import os
import shutil
import time

parser = argparse.ArgumentParser(description="Photo organizer by date.")
parser.add_argument('images_folder', metavar='path', help='Path where the images to be organized are.')
args = parser.parse_args()

index = 0
month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
              'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

for root, _, images in os.walk(args.images_folder):

    for image in images:
        image_path = os.path.join(root, image)

        if root == args.images_folder:
            index += 1
            modified_date = time.ctime(os.path.getmtime(image_path))
            year = modified_date[-4:]
            month = modified_date[4:7]
            month_num = month_dict[month]
            dir_move = os.path.join(args.images_folder, year, month_num)
            os.makedirs(dir_move, exist_ok=True)
            if os.path.isfile(os.path.join(dir_move, image)) is False:
                shutil.copy2(image_path, dir_move)
                print(f'{index} - Copied from {image_path} to {dir_move}')
            else:
                print(f'{index} - File already exists: {image_path} in {dir_move}')

print(f'\nFiles were copied.')
