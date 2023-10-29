import os
import json

def get_files_in_directory(directory):
    file_list = []
    for root, directories, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_list.append(file_path)
    return file_list

def save_files_as_json(directory):
    result = {}
    for root, directories, files in os.walk(directory):
        folder_name = os.path.basename(root)
        file_list = get_files_in_directory(root)
        result[folder_name] = file_list

    with open('files.json', 'w') as json_file:
        json.dump(result, json_file)

# 替换为你的目标目录
target_directory = '.\\'
save_files_as_json(target_directory)
