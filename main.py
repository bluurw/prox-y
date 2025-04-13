import datetime
import time
import os

import panels
import banners
import logger
import agent

while True:
    try:
        banners.blurred_black()
        option_menu = int(panels.menu_panel())
        
        if option_menu == 1:
            while True:
                banners.blurred_black()
                option_generate_proxies = panels.generate_proxy_list_menu_panel()

                if option_generate_proxies == 1:
                    banners.blurred_black()
                    try:
                        file = str(input('What name should output file: '))
                        limit_proxy_results = int(input('How many proxies do you want? '))
                        if limit_proxy_results <= 0:
                            raise ValueError('the number must be greater then 0')
                        
                        data_proxies = agent.proxyGeonode(limit_proxy_results, file)
                        if data_proxies[0]:
                            print('\nProxy validation has been completed')
                            print(f'This was the generate file: {file}\n')
                            break
                        else:
                            print(f'Erro: {data_proxies[1]}')
                            input('...PRESS ANY KEY...')
                    except ValueError as err:
                        banners.blurred_black()
                        print(f'Value Error')
                        input('...PRESS ANY KEY...')
                    except Exception as err:
                        banners.blurred_black()
                        print(err)
                        input('...PRESS ANY KEY...')
                
                elif option_generate_proxies == 2:
                    banners.blurred_black()
                    try:
                        file = str(input('What name should output file: '))
                        limit_proxy_results = int(input('How many proxies do you want? '))
                        if limit_proxy_results <= 0:
                            raise ValueError('the number must be greater then 0')
                        
                        data_proxies = agent.proxyScrape(limit_proxy_results, file)
                        if data_proxies[0]:
                            print('\nProxy validation has been completed')
                            print(f'This was the generate file: {file}\n')
                            break
                        else:
                            print(f'Erro: {data_proxies[1]}')
                            input('...PRESS ANY KEY...')
                    except ValueError as err:
                        banners.blurred_black()
                        print(f'Value Error')
                        input('...PRESS ANY KEY...')
                    except Exception as err:
                        banners.blurred_black()
                        print(err)
                        input('...PRESS ANY KEY...')
                
                elif option_generate_proxies == 0:
                    break
                
                else:
                    input("...PRESS ANY KEY...")

        elif option_menu == 2:
            banners.blurred_black()
            print('TEST_PROXIES')
            file_path = str(input('Inform the JSON path with proxies: '))
            if not file_path.endswith('.json'):
                file_path = file_path + '.json'
                if os.path.exists(file_path):
                    file_path_save = str(input('Inform the JSON path for validated proxies: '))
                    if not file_path_save.endswith('.json'):
                        file_path_save = file_path_save + '.json'

                    for proxy in logger.jsonRead(file_path):
                        time_now_start_validate = datetime.datetime.now()
                        print(f'>> {proxy["ip"]}:{proxy["port"]} VALIDATE:{proxy["validated"]} SSL:{proxy["ssl"]}')
                        validate_proxy = agent.proxyV(proxy)
                        print(f'>> {proxy["ip"]}:{proxy["port"]} VALIDATE:{validate_proxy["validated"]} SSL:{validate_proxy["ssl"]}\n')

                        if validate_proxy['validated']:
                            logger.jsonWrite(validate_proxy, save_file=file_path_save)
                            logger.jsonWrite(validate_proxy, save_file='history-proxy-info.json', history=True) # nao alterar
                        else:
                            logger.jsonWrite(validate_proxy, save_file='history-proxy-info.json', history=True) # nao alterar
                
                    print('\nProxy validation has been completed')
                    print(f'This was the generated file: {file_path_save}\n')
                    input('...PRESS ANY KEY...')
                else:
                    banners.blurred_black()
                    print(f'Invalid path! {file_path}')
                    input('...PRESS ANY KEY...')

        elif option_menu == 3:
            banners.blurred_black()
            panels.about_me()

        elif option_menu == 0:
            banners.exit_black_outline_banner()
            time.sleep(2.5)
            break

        else:
            banners.block_two_lines()
            print('There is nothing here.')
            input('...PRESS ANY KEY...')
    
    except ValueError:
        input('...PRESS ANY KEY...')
    except Exception as err:
        print(err)
        input('...PRESS ANY KEY...')
