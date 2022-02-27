#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
# Obtaining username from environment variables:
user = os.getenv('USER')
image_dir = f'/home/{user}/supplier-data/images/'
# Listing files:
files = os.listdir(image_dir)
for file_name in files:
    # Check if .jpeg image:
    if 'jpeg' in file_name:
        if file_name.split('.')[1] == 'jpeg':
            image_path = image_dir + file_name
            # uploading image:
            with open(image_path, 'rb') as opened_image:
                r = requests.post(url, files={'file': opened_image})
