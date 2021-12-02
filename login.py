from selenium import webdriver
from time import sleep
import traceback


#input email
#search cookies with that email in filename
#launch driver with those cookies
#you're loged in in that account


COOKIES_FOLDER = 'cookies_folder'
COOKIES_FOLDER = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\login and launcher\cookies_folder'
#v96
EXECUTABLE_PATH = 'chromedriver.exe'


# def save_cookies(d, COOKIES_FILENAME_MAIL):
#     ''' d, COOKIES_FILE // if COOKIES_FILE name not specified = cookies_last_login.pkl '''
#     import pickle
    
#     COOKIES_FILE_PATH = COOKIES_FOLDER + '\\' + COOKIES_FILENAME_MAIL+ '.pkl'
#     with open(COOKIES_FILE_PATH, "wb") as f:
#         pickle.dump( d.get_cookies(), f)


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


def get_cookies_filepath(account_mail, google_or_walla):
    import os
    global COOKIES_FOLDER
    
    all_cookie_files = os.listdir(COOKIES_FOLDER)
    for file_path in all_cookie_files:
        print(file_path)
        #filepath= google+mail or walla+mail. Use google_or_walla to distinguish
        # if account_mail in file_path and google_or_walla in file_path:
        if account_mail in file_path:
            print(f'he encontrado este archivo de cookies {file_path}')
            return file_path
    #if no matches
    print(f'not founded any cookies file for this g_account {account_mail}')
    return 'file not found'

def my_get(d, url):
    from selenium.common.exceptions import TimeoutException
    # print(f'going to get {url}')
    try:
        d.get(url)
        # print('url got')
    except TimeoutException as timeout:
        print('time out exception in get, getting again')
        d.get(url)

def close_window(d):
    if len(d.window_handles) != 1:
        first_winodw = d.window_handles[0]
        second_winodw = d.window_handles[1]
        
        d.switch_to.window(first_winodw)
        d.close()
        sleep(2)
        d.switch_to.window(second_winodw)


def run():

    for _ in range(100):

        #loop to ask user walla or mila and set the target url
        while True: #walla or mila variable is also used to differenciate between cookies from walla and mila
            walla_mila = input('\n ¿ quieres logerte en wallapop o en milanuncios ?, responde walla o mila : ')
            if walla_mila == 'walla':
                url = 'https://es.wallapop.com/'
                break
            elif walla_mila == 'mila':
                url = 'https://www.milanuncios.com/'
                break
        
        #ask for the target email account to login
        mail = input('pon aqui email a la que quieres hacer login y pulsa enter: ')
        
        #get cookies file using that email and walla_or_mila cookies
        cookies_file = get_cookies_filepath(mail, walla_mila)
        if cookies_file == 'file not found':
            print('No he encontrado archivo de cookies para ese correo')
            continue #start another iteration

        #set driver
        import undetected_chromedriver.v2 as uc
        options = uc.ChromeOptions()
        # d = uc.Chrome(executable_path=EXECUTABLE_PATH,options=options)
        d = uc.Chrome(options=options)
        d.set_page_load_timeout(5) #sometimes it gets stuck. Used with timeout exception ro get again current url and avoid the stuck

        #login with cookies
        with d:

            login_cookies(d, url, cookies_file)

            #close anoying window
            close_window(d)

            # save_cookies(d, filename)


if __name__ == '__main__':
    run()
