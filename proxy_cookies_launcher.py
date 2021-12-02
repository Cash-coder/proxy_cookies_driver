from time import sleep

def set_driver():
    import proxy_data 
    import undetected_chromedriver.v2 as uc
    # import proxy_data #py file

    # PROXY SETTINGS
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

    IP2 = proxy_data.IP_LIST[1]
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

d = set_driver()
sleep(1000)