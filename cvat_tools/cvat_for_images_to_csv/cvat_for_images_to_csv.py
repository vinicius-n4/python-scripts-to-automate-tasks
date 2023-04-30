import argparse
import zipfile
from bs4 import BeautifulSoup
import csv
import os

parser = argparse.ArgumentParser(description="Convert CVAT for images to a simple CSV.")
parser.add_argument('zip_xml_path', metavar='file', help='The .zip or .xml CSV for images path.')
args = parser.parse_args()

path_save = os.path.join(os.path.dirname(args.zip_xml_path), os.path.basename(args.zip_xml_path) + '_CSV')
os.makedirs(os.path.join(path_save), exist_ok=True)
result_list = []
index = 1

for root, _, files in os.walk(args.zip_xml_path):
    for file in files:
        try:
            with zipfile.ZipFile(os.path.join(root, file)) as z:
                z.extractall(root)
                with open(os.path.join(root, 'annotations.xml'), 'r') as xml:
                    data = xml.read()
        except:
            with open(os.path.join(root, file), 'r') as xml:
                data = xml.read()

        bs_data = BeautifulSoup(data, 'xml')
        all_tag = bs_data.find_all('tag')
        result_list.append(all_tag)
        print(f'{index} Read: {file}')
        index += 1

with open(os.path.join(path_save, 'result_data.csv'), 'w') as csvfile:
    field_names = ['nome_do_arquivo', 'resposta_da_anotação']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for r in result_list:
        for i in r:
            path = os.path.basename(i.parent.get('name'))
            writer.writerow({'nome_do_arquivo': path, 'resposta_da_anotação': i.get('label')})
