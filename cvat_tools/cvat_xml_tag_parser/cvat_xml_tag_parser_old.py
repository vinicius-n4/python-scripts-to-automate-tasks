# reference: https://linuxhint.com/parse_xml_python_beautifulsoup/

from bs4 import BeautifulSoup
import argparse

spoof_qnt = 0
undefined_qnt = 0
live_qnt = 0
repeated_label = []
repeated_list = []
empty_list = []

parser = argparse.ArgumentParser(description="Get the spoof ID from a CVAT xml export.")
parser.add_argument('xml_path', metavar='file', help='The xml file path.')
args = parser.parse_args()

with open(args.xml_path, 'r') as xml:
    data = xml.read()
bs_data = BeautifulSoup(data, 'xml')
live_tag = bs_data.find_all('tag', {'label': 'live'})
spoof_tag = bs_data.find_all('tag', {'label': 'spoof'})
undefined_tag = bs_data.find_all('tag', {'label': 'undefined'})
empty_tag = bs_data.find_all('tag', {'label': ''})

live_txt = open('live_id.txt', 'w')
for tag in live_tag:
    live_id = tag.parent.get('id')
    live_txt.write(f'live - {live_id}\n')
    repeated_label.append(live_id)
    live_qnt += 1
print(f'\nThere are {live_qnt} live images in this batch.')
live_txt.close()

spoof_txt = open('spoof_id.txt', 'w')
for tag in spoof_tag:
    spoof_id = tag.parent.get('id')
    spoof_txt.write(f'spoof - {spoof_id}\n')
    repeated_label.append(spoof_id)
    spoof_qnt += 1
print(f'There are {spoof_qnt} spoof images in this batch.')
spoof_txt.close()

undefined_txt = open('undefined_id.txt', 'w')
for tag in undefined_tag:
    undefined_id = tag.parent.get('id')
    undefined_txt.write(f'undefined - {undefined_id}\n')
    repeated_label.append(undefined_id)
    undefined_qnt += 1
print(f'There are {undefined_qnt} undefined images in this batch.')
undefined_txt.close()

# Repeated labels:
for i in repeated_label:
    if repeated_label.count(i) > 1:
        repeated_list.append(i)
        while repeated_label.count(i) > 1:
            index = repeated_label.index(i)
            repeated_label.pop(index)
print(f'\nThere are {len(repeated_list)} repeated labels: {repeated_list}')

# Empty labels:
for tag in empty_tag:
    empty_id = tag.parent.get('id')
    empty_list.append(empty_id)
print(f'There are {len(empty_list)} images without label: {empty_list}\n')

print('Logs were saved in the same directory as the cvat_xml_tag_parser.py.\n')
xml.close()
