import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="Move files into batches.")
parser.add_argument('--path', required=True, help='The path to a directory containing files.')
args = parser.parse_args()

index = 0

for root, _, files in os.walk(args.path):
    for file in files:
        copy_to = os.path.join(os.path.dirname(root), f'lote_{index}')
        os.makedirs(copy_to, exist_ok=True)
        shutil.copy2(os.path.join(root, file), copy_to)
        qnt_files = len(os.listdir(copy_to))
        if qnt_files == 5000:
            index += 1
