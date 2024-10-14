import sys
import os
from PIL import Image

image_folder = sys.argv[1]
converted_folder_name = sys.argv[2]

try:
    image_list = os.listdir(image_folder)
    if not os.path.exists(converted_folder_name):
        os.makedirs(converted_folder_name)
    if len(image_list):
        for image in image_list:
            img = Image.open(f'./{image_folder}/{image}')
            clean_name = os.path.splitext(image)[0]
            img = img.save(f'{converted_folder_name}/{clean_name}.png', 'png')

except TypeError as err:
    print("Error: Input string")
    raise err
except FileNotFoundError as err:
    print("Error: File not found")
    raise err
except:
    print("Error: Invalid input")
