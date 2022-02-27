#!/usr/bin/env python3

import os
from PIL import Image, UnidentifiedImageError


user = os.getenv('USER')
image_dir = f'/home/{user}/supplier-data/images/'
for file_name in os.listdir(image_dir):
    file = image_dir + file_name
    if os.path.isfile(file):
        try:
            path = os.path.splitext(file)[0]
            with Image.open(file) as im:
                im_path = f'{path}.jpeg'
                im.convert('RGB').resize((600, 400)).save(im_path, "JPEG")
        except UnidentifiedImageError:  # Wrong file type: continue
            continue
