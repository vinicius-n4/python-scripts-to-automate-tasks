# concat_images
Scripts that concatenate two or three images in line from a source image folder.

## Usage
1. Download the scripts or clone the repository;
2. Run the script using the avaiable arguments:
- `--path_images`: path to the folder containing raw images;
- `--dir_save`: path to the folder where output images are stored;
- `--csv_file`: csv file with img1 path and img2 path (optional);

```bash
python3 concat_two_images.py --path_images /path/to/images --dir_save /path/to/save
```

## Reference
- [Python Pillow Paste](https://note.nkmk.me/en/python-pillow-paste/https://note.nkmk.me/en/python-pillow-concat-images/)
 