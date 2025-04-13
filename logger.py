import datetime
import json
import os

def jsonWrite(proxy, save_file, history=False):
    temp_file = save_file + '.tmp'
    try:
        with open(save_file, 'r') as f:
            data = json.load(f)
    # se nao existe, abre um zerado
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if history:
        data.append(proxy)
    else:
        for item in data:
            if proxy['ip'] in item.values() and proxy['port'] in item.values():
                item['updated'] = proxy['updated']
        else:
            data.append(proxy)
    try:
        with open(temp_file, 'w') as f:
            json.dump(data, f, indent=4)
        os.replace(temp_file, save_file)
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def jsonRead(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception as err:
        return False, err