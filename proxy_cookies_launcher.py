from time import sleep
import traceback


#type account email name and set the proxy number to log into that account

#given mail, return filepath of walla_cookies_file of that mail

COOKIES_FOLDER  = 'cookies_folder'
ACCOUNT_EMAIL   = 'dkenji589@gmail.com' #using this has Madrid  instead of Valencia
PROXY_NUMBER    = 1
URL = 'https://es.wallapop.com/app/catalog/list'


def get_cookies_filepath(account_mail, walla_mila):
    import os
    global COOKIES_FOLDER

    #redo:
    # using just one folder for all cookies file
    # all names with walla or mila at beginning

    # files = load all files from folder
    # for file_name in files:
        # if walla_mila in file_name and account_mail in file_name:
            # return file_name
    # if reach this point = no matches; return no matches 

    # --- #
    #current
    #list all files in cookies_folder
    #mila cookies should have mila in the filename but they haven't it yet
    # use walla_mila to know what cookies file to pick.
    #if mila in walla_mila:
        # For file_path in cookies_folder:
            # if account_mail and walla_mila in filepth: (Now only account_mail, no mila in filenames)
                #return that filepath
    #same for walla
    
    all_cookie_files = os.listdir(COOKIES_FOLDER)

    if walla_mila == 'mila':
        for file_path in all_cookie_files:
            print(file_path)
            #filepath= google+mail or walla+mail. Use walla_mila to distinguish
            # if account_mail in file_path and walla_mila in file_path:
            if account_mail in file_path:
                print(f'he encontrado este archivo de cookies {file_path}')
                return file_path
        #if no matches
        print(f'not founded any cookies file for this g_account {account_mail}')
        return 'file not found'

    elif walla_mila == 'walla':
        for file_path in all_cookie_files:
            if account_mail in file_path and walla_mila in file_path:
                print(f'he encontrado este archivo de cookies {file_path}')
                return file_path
        #if no matches
        print(f'not founded any cookies file for this g_account {account_mail}')
        return 'file not found'



def set_driver():
    import proxy_data 
    import undetected_chromedriver.v2 as uc
    # import proxy_data #py file

    # PROXY SETTINGS TO ITERATE IP's
    # global n_proxy
    # IP_LIST = proxy_data.IP_LIST
    # USER    = proxy_data.USER
    # PASS    = proxy_data.PASS
    # SOCKS5_PORT  = proxy_data.SOCKS5_PORT
    # # get the next ip of the list
    # if n_proxy == 10: #reset
    #     n_proxy = 0
    # NEXT_IP = IP_LIST[n_proxy]
    # n_proxy +=1

    EXECUTABLE_PATH = 'chromedriver.exe'
    IP2 = proxy_data.IP_LIST[PROXY_NUMBER]
    SOCKS5_PORT  = proxy_data.SOCKS5_PORT

    options = uc.ChromeOptions()
    # options.add_argument(f'--proxy-server=socks5://{IP}:{HTTPS_PORT}')
    # options.add_argument(f'--proxy-server=https://{IP}:{HTTPS_PORT}')
    options.add_argument(f'--proxy-server=socks5://{IP2}:{SOCKS5_PORT}')

    # options.add_argument("start-maximized")

    d = uc.Chrome(executable_path=EXECUTABLE_PATH, options=options)
    d.maximize_window()
    d.set_page_load_timeout(15) 

    return d

def login_cookies(d, url, cookies_filename):
    import pickle

    #create path to folder    
    cookies_filepath = COOKIES_FOLDER + '\\' + cookies_filename
    print(f'this is cookies_filepath {cookies_filepath} \n and url {url}')
    try:
        d.get(url)
        cookies = pickle.load(open(cookies_filepath, "rb"))
        for cookie in cookies:
            if 'sameSite' in cookie:
                if cookie['sameSite'] == 'None':
                    cookie['sameSite'] = 'Strict'
            d.add_cookie(cookie)
            # print(cookie)
            
        my_get(d, url)
        # d.get(url)

    except Exception as e:
        print('exception in login cookies:',e)
        traceback.print_exc()

def my_get(d, url):
    from selenium.common.exceptions import TimeoutException
    # print(f'going to get {url}')
    try:
        d.get(url)
        # print('url got')
    except TimeoutException as timeout:
        print('time out exception in get, getting again')
        d.get(url)


def run():

    d = set_driver()
    cookies_file = get_cookies_filepath(ACCOUNT_EMAIL, 'walla')
    print(cookies_file)

    login_cookies(d, URL, cookies_file)

    sleep(10000)


if __name__ == '__main__':
    run()