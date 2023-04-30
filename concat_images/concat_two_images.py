import argparse
import csv
import os

from PIL import Image


success_list = []
fails_list = []
empty_folders = []

parser = argparse.ArgumentParser(description='Merge images from folder.')
parser.add_argument('--path_images', required=True, help='path to the folder containing raw images.')
parser.add_argument('--dir_save', required=True, help='path to the folder where output images are stored.')
parser.add_argument('--csv_file', required=False, default=None, help='csv file with img1 path and img2 path.')
args = parser.parse_args()

os.makedirs(args.dir_save, exist_ok=True)


def join_images(images_path, output_path):
    index = 1

    for root, _, files in os.walk(images_path):

        folder = os.path.basename(root)

        if len(files) >= 2:

            # Open image:
            st_path = os.path.join(root, files[0])
            st_image = Image.open(st_path)

            nd_path = os.path.join(root, files[1])
            nd_image = Image.open(nd_path)

            # Create an empty image:
            concat = Image.new('RGB', (st_image.width + nd_image.width, max(st_image.height, nd_image.height)))

            # Paste image, biggest first:
            if st_image.height > nd_image.height:
                concat.paste(st_image, (0, 0))
                concat.paste(nd_image, (st_image.width, round((st_image.height - nd_image.height) / 2)))
            else:
                concat.paste(nd_image, (0, 0))
                concat.paste(st_image, (nd_image.width, round((nd_image.height - st_image.height) / 2)))

            # Save image:
            concat.save(os.path.join(output_path, f'{folder}.jpg'))

            success_list.append(os.path.join(root, folder))
            print(f'{index} - Image Concatenated:', os.path.join(output_path, f'{folder}.jpg'))
            index += 1

        elif len(files) == 0:
            empty_folders.append(os.path.join(root, folder))
            print(f'{index} - This folder is empty:', os.path.join(root, folder))
            index += 1

        else:
            fails_list.append(os.path.join(root, folder))
            print(f'{index} - Process Failed:', os.path.join(root, folder))
            index += 1


def csv_join_images(images_path, output_path, csv_file):
    index = 1

    for root, _, files in os.walk(images_path):
        if len(files) > 1:

            with open(csv_file, 'r') as file:
                csvreader = csv.reader(file, delimiter=',')

                for row in csvreader:
                    # Open image:
                    st_path = os.path.join(root, row[1])
                    if os.path.isfile(st_path):
                        st_image = Image.open(st_path)
                    else:
                        fails_list.append(row[0])
                        print(f'{index} - File is irregular or doesn\'t exist:', row[0])
                        index += 1
                        continue

                    nd_path = os.path.join(root, row[2])
                    if os.path.isfile(nd_path):
                        nd_image = Image.open(nd_path)
                    else:
                        fails_list.append(row[0])
                        print(f'{index} - File is irregular or doesn\'t exist:', row[0])
                        index += 1
                        continue

                    # Create an empty image:
                    concat = Image.new('RGB', (st_image.width + nd_image.width, max(st_image.height, nd_image.height)))

                    # Paste image, biggest first:
                    if st_image.height > nd_image.height:
                        concat.paste(st_image, (0, 0))
                        concat.paste(nd_image, (st_image.width, round((st_image.height - nd_image.height) / 2)))
                    else:
                        concat.paste(nd_image, (0, 0))
                        concat.paste(st_image, (nd_image.width, round((nd_image.height - st_image.height) / 2)))

                    # Save image:
                    concat.save(os.path.join(output_path, f'{row[0]}.jpg'))

                    success_list.append(os.path.join(output_path, f'{row[0]}.jpg'))
                    print(f'{index} - Image Concatenated:', os.path.join(output_path, f'{row[0]}.jpg'))
                    index += 1

        elif len(files) <= 1:
            empty_folders.append(root)
            print(f'{index} - This folder is empty or there\'re less than two images:', root)
            index += 1
            continue

        else:
            fails_list.append(row[0])
            print(f'{index} - Fail to concatenate:', row[0])
            break


if args.csv_file is None:
    join_images(args.path_images, args.dir_save)
else:
    csv_join_images(args.path_images, args.dir_save, args.csv_file)

print(f'\nSUCCESS: {len(success_list)} images')
print(f'EMPTY FOLDERS: {len(empty_folders)} folders')
print(f'FAILS: {len(fails_list)} items: {fails_list}\n')
