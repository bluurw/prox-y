import datetime
import json

def jsonWrite(proxy, file='proxy-info.json', history=False):
    try:
        with open(file, 'r') as f:
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
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    
    return f'Proxy inserted in {file}'