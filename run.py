#!/usr/bin/env python3

import os
import requests


def catalog_data(website, target_dir):
    """This function will return a list of dictionaries"""
    fruit = {}
    for file_name in os.listdir(target_dir):
        fruit.clear()
        filename = os.path.join(target_dir, file_name)
        with open(filename) as f:
            line = f.readlines()
            description = ""
            for i in range(2, len(line)):
                description = description + line[i].strip('\n').replace(u'\xa0', u'')
            fruit["description"] = description
            fruit["weight"] = int(line[1].strip('\n').strip('lbs'))
            fruit["name"] = line[0].strip('\n')
            fruit["image_name"] = (file_name.strip('.txt')) + '.jpeg'
            print(fruit)
            if website != "":
                response = requests.post(website, json=fruit)
                print(response.request.url)
                print(response.status_code)
    return 0


if __name__ == '__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    description_dir = f'/home/{user}/supplier-data/descriptions/'
    catalog_data(url, description_dir)
    