import undetected_chromedriver.v2 as uc
import proxy_data
from time import sleep

EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\login and launcher\chromedriver.exe'

COOKIES_FOLDER  = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\login and launcher\cookies_folder\\'
SITE_URL        = 'https://es.wallapop.com/'


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

    print('saving cookies')

    if city == 'unspecified':
        city = "cookies_last_login.pkl" 
    
    COOKIES_FILE_PATH = COOKIES_FOLDER + '\\' + city + '.pkl'

    with open(COOKIES_FILE_PATH, "wb") as f:
        pickle.dump(d.get_cookies(), f)
    print(f'login cookies saved in city file {city}')


def load_cookies(d, city):
    import pickle

    cookies_filepath = f'{COOKIES_FOLDER}{city}.pkl'

    # driver has to be in the target URL in order to load the cookies
    d.get(SITE_URL)

    cookies = pickle.load(open(cookies_filepath, "rb"))
    for cookie in cookies:
        if cookie['domain'] == '.wallapop.com':
            d.add_cookie(cookie)
            print(f'added this cookie: {cookie}')

    # to apply effect of the cookies reload the page
    sleep(5)
    d.get(SITE_URL)

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
        a = input('Enter return to continue ')
        if a == '':
            print('Capted a break')
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

        close_second_tab(d)

        load_cookies(d, city)

        # d2 = set_driver(1)
        # d2.get(SITE_URL)
        # opened_drivers.append([d, city])

        my_wait()
        
        save_cookies(d, city)

    # save_all_cookies(opened_drivers)

if __name__ == '__main__':
    run()