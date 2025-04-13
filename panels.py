def menu_panel():
    print('''
PROXY_LIST_MENU
[1] - Generate_list
[2] - Test_Proxies
[3] - About_me
[0] - Exit
    ''')
    option = int(input('Enter the desired option: '))
    return option

def generate_proxy_list_menu_panel():
    print('''
PROXY_LIST_GENERATOR
[1] - Geonode
[2] - Scrape
[0] - Return
    ''')
    option = int(input('Enter the desired option: '))
    return option

def about_me():
    print('ABOUT_ME')
    print('The macaws above my head dont let me think.')

    print('#SOCIAL')
    print('Github: https://github.com/bluurw')
    print('Telegram: https://t.me/mk_Directory')
    print()
    input('...PRESS ANY KEY...')