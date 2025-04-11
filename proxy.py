import logger

import requests
import datetime

# implantar um limite
def proxyGeonode(save_file='proxy-info.json'):
    limit=500
    page = 1
    while True:
        r = requests.get(f'https://proxylist.geonode.com/api/proxy-list?limit={limit}&page={page}&sort_by=lastChecked&sort_type=desc')
        if r.status_code == 200:
            js = r.json()
            if len(js['data']) != 0:
                for proxy in js['data']:
                    now = datetime.datetime.now()
                    proxy_info = {
                        'ip': proxy['ip'],
                        'port': proxy['port'],
                        'anonymityLevel': proxy['anonymityLevel'],
                        'country': proxy['country'],
                        'city': proxy['city'],
                        'isp': proxy['isp'],
                        'protocols': proxy['protocols'],
                        'api_proxy': 'geonode',
                        'updated': now.strftime("%H:%M:%S %d/%m/%Y")
                    }
                    logger.jsonWrite(proxy_info, file=save_file)
                    logger.jsonWrite(proxy_info, file='history-proxy-info.json', history=True)
                page +=1
            else:
                break

# implantar um limite
def proxyScrape(save_file='proxy-info.json'):
    r = requests.get('https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json')
    if r.status_code == 200:
        js = r.json()
        for proxy in js['proxies']:
            now = datetime.datetime.now()
            try:
                proxy_info = {
                    'ip': proxy['ip'],
                    'port': proxy['port'],
                    'anonymityLevel': proxy['anonymity'],
                    'country': proxy['ip_data']['countryCode'],
                    'city': proxy['ip_data']['city'],
                    'isp': proxy['ip_data']['isp'],
                    'protocols': proxy['protocol'],
                    'api_proxy': 'proxyscrape',
                    'updated': now.strftime("%H:%M:%S %d/%m/%Y")
                }
            except KeyError as err:
                continue
            logger.jsonWrite(proxy_info, file=save_file)
            logger.jsonWrite(proxy_info, file='history-proxy-info.json', history=True)