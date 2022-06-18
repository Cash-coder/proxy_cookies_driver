import undetected_chromedriver.v2 as uc
import proxy_data
from time import sleep

PROXY           = "185.239.140.165:49155"
EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'
COOKIES_FOLDER  = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\login and launcher\cookies_folder\\'


def set_driver(proxy_n):

    import proxy_data

    IP_ENTRY  = proxy_data.IP_DICT[proxy_n]
    IP        = IP_ENTRY.get('ip')
    CITY      = IP_ENTRY.get('city')

    HTTPS_PORT = proxy_data.HTTPS_PORT

    options = uc.ChromeOptions()
    options.add_argument(f'--proxy-server=http://{IP}:{HTTPS_PORT}')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

    d = uc.Chrome(executable_path=EXECUTABLE_PATH, options=options)
    d.maximize_window()

    return d, CITY


def save_cookies(d, city='unspecified'):
    ''' d, city // if city name not specified = cookies_last_login.pkl '''
    import pickle

    if city == 'unspecified':
        city = "cookies_last_login.pkl" 
    
    COOKIES_FILE_PATH = COOKIES_FOLDER + '\\' + city + '.pkl'

    with open(COOKIES_FILE_PATH, "wb") as f:
        pickle.dump( d.get_cookies(), f)
    print(f'login cookies saved in city file {city}')


def load_cookies(d, city):
    import pickle

    cookies_filepath = f'{COOKIES_FOLDER}{city}.pkl'

    d.get('https://es.wallapop.com/')

    cookies = pickle.load(open(cookies_filepath, "rb"))
    for cookie in cookies:
        if cookie['domain'] == '.wallapop.com':
        # if google_or_walla in cookie['domain']:
            d.add_cookie(cookie)
            print(f'added this cookie: {cookie}')

    d.get('https://es.wallapop.com/')

    return d


def close_second_tab(d):
    if len(d.window_handles) != 1:
        first_winodw = d.window_handles[0]
        second_winodw = d.window_handles[1]
        
        d.switch_to.window(first_winodw)
        d.close()
        
        # back to where you were
        sleep(1)
        d.switch_to.window(second_winodw)

def my_wait():
    while True:
        try:
            # a = input('Do you want to save cookies? ')
            sleep(100000)
        except KeyboardInterrupt:
            print('Capted a break, saving cookies')
            return

def run():

    # opened_drivers = []
    for i in range(5):

        i = input('eneter proxy n: ')
        print('selected input is: ', i)

        # made to skip proxies and go to save_all_cookies()
        if i == '':
            print('passed')
            continue
        else:
            i = int(i)

        d, city = set_driver(i)

        load_cookies(d, city)

        close_second_tab(d)

        # d2 = set_driver(1)
        # d2.get('https://es.wallapop.com/')
        # opened_drivers.append([d, city])

        my_wait()
        
        save_cookies(d, city)

    # save_all_cookies(opened_drivers)

if __name__ == '__main__':
    run()