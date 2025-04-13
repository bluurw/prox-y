import requests
import datetime

import logger

def proxyV(data):
    proxies = [
        {"http": f'http://{data["ip"]}:{data["port"]}'},
        {"https": f'https://{data["ip"]}:{data["port"]}'}
    ]
    now = datetime.datetime.now()
    for proxy in proxies:   
        try:
            response = requests.get("http://httpbin.org/ip", proxies=proxy, timeout=10)
            if response.status_code == 200:
                data['validated'] = True
                data['ssl'] = 'https' in proxy
                data['updated'] = now.strftime("%H:%M:%S %d/%m/%Y")
                variation = datetime.datetime.now() - now
                data['time_variation_validate'] = variation.total_seconds()
                return data
        except requests.exceptions.RequestException:
            continue
    data['validated'] = False
    data['ssl'] = False
    data['updated'] = now.strftime("%H:%M:%S %d/%m/%Y")
    data['time_variation_validate'] = datetime.datetime.now() - now
    return data

def proxyGeonode(limit_proxy_results, save_file='proxy-info.json'):
    if not save_file.endswith('.json'):
        save_file = save_file + '.json'
    page = 1
    while limit_proxy_results > 0:
        r = requests.get(f'https://proxylist.geonode.com/api/proxy-list?limit=500&page={page}&sort_by=lastChecked&sort_type=desc')
        if r.status_code == 200:
            js = r.json()
            if 'data' in js and len(js['data']) != 0:
                for proxy in js['data']:
                    if limit_proxy_results <= 0:
                        break
                    now = datetime.datetime.now()
                    try:
                        proxy_info = {
                            'ip': proxy['ip'],
                            'port': proxy['port'],
                            'anonymityLevel': proxy['anonymityLevel'],
                            'country': proxy.get('country', 'Unknown'),
                            'city': proxy.get('city', 'Unknown'),
                            'isp': proxy.get('isp', 'Unknown'),
                            'protocols': proxy.get('protocols', []),
                            'ssl': False,
                            'api_proxy': 'geonode',
                            'validated': False,
                            'updated': now.strftime("%H:%M:%S %d/%m/%Y")
                        }
                    except KeyError as err:
                        print(f">> Missing Key: {err}")
                        continue
                    
                    print(f'>> {proxy["ip"]}:{proxy["port"]}')
                    logger.jsonWrite(proxy_info, save_file=save_file)
                    logger.jsonWrite(proxy_info, save_file='history-proxy-info.json', history=True)
                    
                    limit_proxy_results -= 1
                page += 1
            else:
                return False, 'No data Found'
        else:
            return False, f'Problem encountered while requesting {r.status_code}'

def proxyScrape(limit_proxy_results, save_file='proxy-info.json'):
    if not save_file.endswith('.json'):
        save_file = save_file + '.json'
    
    r = requests.get('https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json')
    
    if r.status_code == 200:
        try:
            js = r.json()  # Conversao
            if 'proxies' in js and len(js['proxies']) > 0:
                for proxy in js['proxies']:
                    if limit_proxy_results > 0:
                        now = datetime.datetime.now()
                        try:
                            proxy_info = {
                                'ip': proxy.get('ip', 'Unknown'),
                                'port': proxy.get('port', 'Unknown'),
                                'anonymityLevel': proxy.get('anonymity', 'Unknown'),
                                'country': proxy.get('ip_data', {}).get('countryCode', 'Unknown'),
                                'city': proxy.get('ip_data', {}).get('city', 'Unknown'),
                                'isp': proxy.get('ip_data', {}).get('isp', 'Unknown'),
                                'protocols': proxy.get('protocol', []),
                                'ssl': False,
                                'api_proxy': 'proxyscrape',
                                'validated': False,
                                'updated': now.strftime("%H:%M:%S %d/%m/%Y")
                            }
                        except KeyError as err:
                            print(f">> Missing Key: {err}")
                            continue

                        print(f'>> {proxy_info["ip"]}:{proxy_info["port"]}')
                        logger.jsonWrite(proxy_info, save_file=save_file)
                        logger.jsonWrite(proxy_info, save_file='history-proxy-info.json', history=True)
                        limit_proxy_results -= 1
                    else:
                        break
            else:
                return False, 'No data Found'
        except ValueError:
            return False, 'Error processing JSON'
    else:
        return False, f'Problem encountered while requesting {r.status_code}'