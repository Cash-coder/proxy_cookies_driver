from time import sleep
import proxy_data
import undetected_chromedriver.v2 as uc

from selenium import webdriver
from time import sleep

# https:  49155
# socks5: 49156

# EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'
# IP = '185.239.140.165'
# SOCKS5_PORT  = 49162
# HTTPS_PORT   = 49161

# USER = 'smartmarketer31'
# PASS = 'AtnHbsqvjj'


# from selenium import webdriver

# PROXY = "185.239.140.165:49155"
# PROXY_SOCKS = "185.239.140.85':49156"



# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager




# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome_options.add_argument(f'--proxy-server=http://{PROXY}')
# # chrome_options.add_argument(f'--proxy-server=https://{PROXY}')
# # chrome_options.add_argument('--proxy-server=socks5://185.239.140.85:49162')
# chrome_options.add_argument("ignore-certificate-errors")

# # d = webdriver.Chrome(executable_path=EXECUTABLE_PATH,options=chrome_options)
# d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# d.set_page_load_timeout(15) 
# # d.get("https://www.ipchicken.com/")
# d.get("https://www.google.com/")

# sleep(1000)

#############
# ip_port = "185.239.140.165:49161"
# from selenium import webdriver
# #proxy server definition
# py = "185.239.140.165:49161"

# #configure ChromeOptions class
# chrome_options = webdriver.ChromeOptions()
# #proxy parameter to options
# chrome_options.add_argument('--proxy-server=185.239.140.165:49161')
# #options to Chrome()
# driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH,chrome_options= chrome_options)
# driver.implicitly_wait(0.6)
# driver.get("https://www.tutorialspoint.com/index.htm")



# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % ip_port)
# driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH,chrome_options=chrome_options)

# driver.get('https://www.myexternalip.com/raw')
# sleep(999)


def a():

    PROXY = "185.239.140.165:49155"

    EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'
    # IP = proxy_data.IP_LIST[proxy_n]
    # HTTPS_PORT   = proxy_data.HTTPS_PORT
    # SOCKS5_PORT  = proxy_data.SOCKS5_PORT

    # USER = proxy_data.USER
    # PASS = proxy_data.PASS


    # IP = '185.239.140.85'


    import undetected_chromedriver.v2 as uc
    options = uc.ChromeOptions()
    # options.add_argument(f'--proxy-server=socks5://{IP}:{SOCKS5_PORT}')
    # options.add_argument(f'--proxy-server=socks5://185.239.140.165:49162')
    options.add_argument(f'--proxy-server=http://{PROXY}')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    # options.add_argument(f'--proxy-server=http://{IP}:{HTTPS_PORT}')
    d = uc.Chrome(executable_path=EXECUTABLE_PATH, options=options)
    d.get('https://whatismyipaddress.com/')

    sleep(10)

    # d.get(f'https:{IP}:{HTTPS_PORT}@www.whatismyipaddress.com/')

a()

def set_driver(proxy_n):
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

    EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'
    IP = proxy_data.IP_LIST[proxy_n]
    SOCKS5_PORT  = proxy_data.SOCKS5_PORT
    HTTPS_PORT   = proxy_data.HTTPS_PORT
    USER = proxy_data.USER
    PASS = proxy_data.PASS

    print(f'connecting to USER:{USER}: PASS: {PASS} IP: {IP}; HTTPS_PORT {HTTPS_PORT}')

    options = uc.ChromeOptions()
    # options.add_argument(f'--proxy-server=socks5://{IP}:{HTTPS_PORT}')

    # options.add_argument(f'--proxy-server=https://{IP}:{HTTPS_PORT}')
    # options.add_argument(f'--proxy-server=https://{USER}:{PASS}:{IP}:{HTTPS_PORT}')
    # options.add_argument(f'--proxy-server=socks5://{USER}:{PASS}:{IP}:{SOCKS5_PORT}')
    options.add_argument(f'--proxy-server=socks5://{IP}:{SOCKS5_PORT}')

    # options.add_argument("start-maximized")

    d = uc.Chrome(executable_path=EXECUTABLE_PATH, options=options)
    d.maximize_window()
    d.set_page_load_timeout(15) 
    
    # d.DesiredCapabilities.CHROME['acceptSslCerts']=True

    # d.get(f'https:{USER}:{PASS}@www.whatismyipaddress.com/')
    # d.get(f'socks5:{USER}:{PASS}@www.whatismyipaddress.com/')
    
    d.get('https://whatismyipaddress.com/')

    sleep(20)
    return d


def set_driver_2(proxy_n):

    import proxy_data

    from seleniumwire import webdriver

    IP = proxy_data.IP_LIST[proxy_n]
    SOCKS5_PORT  = proxy_data.SOCKS5_PORT
    HTTPS_PORT   = proxy_data.HTTPS_PORT
    USER = proxy_data.USER
    PASS = proxy_data.PASS

    options = {
        'proxy': {
            # 'http': f'http://{USER}:{PASS}@{IP}:{HTTPS_PORT}',
            'https': f'https://{USER}:{PASS}@{IP}:{HTTPS_PORT}',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }



    driver = webdriver.Chrome(seleniumwire_options=options)

def set_driver_3(proxy_n):
    import seleniumwire.undetected_chromedriver as uc
    import proxy_data

    EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'
    IP = proxy_data.IP_LIST[proxy_n]
    SOCKS5_PORT  = proxy_data.SOCKS5_PORT
    HTTPS_PORT   = proxy_data.HTTPS_PORT
    USER = proxy_data.USER
    PASS = proxy_data.PASS


    chrome_options = uc.ChromeOptions()
    
    driver = uc.Chrome(
        options=chrome_options,
        executable_path=EXECUTABLE_PATH,
        seleniumwire_options={
            'proxy': {
                'https': f'https://{USER}:{PASS}@{IP}:{HTTPS_PORT}'
            }
        }
        )
    
    driver.get('https://whatismyipaddress.com/')
    # d = uc.Chrome(executable_path=EXECUTABLE_PATH, options=options)

def set_driver_3(proxy_n):
    import proxy_data
    import undetected_chromedriver.v2 as uc


    EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'
    IP = proxy_data.IP_LIST[proxy_n]
    SOCKS5_PORT  = proxy_data.SOCKS5_PORT
    HTTPS_PORT   = proxy_data.HTTPS_PORT
    USER = proxy_data.USER
    PASS = proxy_data.PASS


# d = set_driver(1)
# d = set_driver_2(1)
# d = set_driver_3(1)
# d = set_driver_3(1)
# d.get('https://whatismyipaddress.com/')
# sleep(10)






#############################################


# import os
# import zipfile

# from selenium import webdriver

# PROXY_HOST = '185.239.140.157'
# PROXY_PORT = 49161 # port
# PROXY_USER = 'smartmarketer31'
# PROXY_PASS = 'AtnHbsqvjj'


# manifest_json = """
# {
#     "version": "1.0.0",
#     "manifest_version": 2,
#     "name": "Chrome Proxy",
#     "permissions": [
#         "proxy",
#         "tabs",
#         "unlimitedStorage",
#         "storage",
#         "<all_urls>",
#         "webRequest",
#         "webRequestBlocking"
#     ],
#     "background": {
#         "scripts": ["background.js"]
#     },
#     "minimum_chrome_version":"22.0.0"
# }
# """

# background_js = """
# var config = {
#         mode: "fixed_servers",
#         rules: {
#         singleProxy: {
#             scheme: "http",
#             host: "%s",
#             port: parseInt(%s)
#         },
#         bypassList: ["localhost"]
#         }
#     };

# chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

# function callbackFn(details) {
#     return {
#         authCredentials: {
#             username: "%s",
#             password: "%s"
#         }
#     };
# }

# chrome.webRequest.onAuthRequired.addListener(
#             callbackFn,
#             {urls: ["<all_urls>"]},
#             ['blocking']
# );
# """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


# def get_chromedriver(use_proxy=False, user_agent=None):
#     EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'

#     path = os.path.dirname(os.path.abspath(__file__))
#     chrome_options = webdriver.ChromeOptions()
#     if use_proxy:
#         pluginfile = 'proxy_auth_plugin.zip'

#         with zipfile.ZipFile(pluginfile, 'w') as zp:
#             zp.writestr("manifest.json", manifest_json)
#             zp.writestr("background.js", background_js)
#         chrome_options.add_extension(pluginfile)
#     if user_agent:
#         chrome_options.add_argument('--user-agent=%s' % user_agent)
#     driver = webdriver.Chrome(
#         executable_path=EXECUTABLE_PATH,
#         # os.path.join(path, 'chromedriver'),
#         chrome_options=chrome_options)
#     return driver

# def main():
#     driver = get_chromedriver(use_proxy=True)
#     #driver.get('https://www.google.com/search?q=my+ip+address')
#     driver.get('https://httpbin.org/ip')

# if __name__ == '__main__':
#     main()



