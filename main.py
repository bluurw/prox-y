import panels
import banners
import proxy

import time

while True:
    banners.blurred_black()
    option_menu = int(panels.menu_panel())
    if option_menu == 1:
        while True:
            banners.blurred_black()
            option_generate_proxies = panels.generate_proxy_list_menu_panel()
            if option_generate_proxies == 1:
                print(proxy.proxyGeonode())
            elif option_generate_proxies == 2:
                print(proxy.proxyGeonode())
            elif option_generate_proxies == 0:
                break
            else:
                continue

    elif option_menu == 2:
        print('Still on development')
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
        print('There is nothing Here')
        input('...PRESS ANY KEY...')

