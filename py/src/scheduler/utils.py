import requests
import json
from .config import Config
import time
import logging
import folder_paths
import base64
import os

def nested_object_to_dict(obj):
    if isinstance(obj, list):
        return [nested_object_to_dict(x) for x in obj]
    if isinstance(obj, dict):
        return {k: nested_object_to_dict(v) for k, v in obj.items()}
    if  obj and type(obj) not in (int, float, str):
        return nested_object_to_dict(vars(obj))
    else:
        return obj

def file_to_base64(filename,type='output', subfolder=None):
    if type=="temp":
        output_dir = folder_paths.get_temp_directory()
    else:
        output_dir = folder_paths.get_output_directory()
    if subfolder:
        file_path=os.path.join(output_dir,subfolder,filename)
    else:
        file_path=os.path.join(output_dir,filename)
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode("utf-8")
 
def base64_to_file(base64_string,filename,type='output', subfolder=None):
    image_data = base64.b64decode(base64_string)
    if type=="temp":
        output_dir = folder_paths.get_temp_directory()
    else:
        output_dir = folder_paths.get_output_directory()
    if subfolder:
        file_path=os.path.join(output_dir,subfolder,filename)
    else:
        file_path=os.path.join(output_dir,filename)
    with open(file_path, 'wb') as file:
        file.write(image_data)
    return filename

def base64_to_b64encode(file_data):
    fileData = base64.b64encode(file_data)
    return fileData.decode("utf-8")

def base64_to_b64decode(base64_string):
    fileData = base64.b64decode(base64_string)
    return fileData

def base64_encode(text):
    '''加密'''
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded_text


def base64_decode(encoded_text):
    '''解密'''
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    return decoded_text
