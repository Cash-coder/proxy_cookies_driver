import undetected_chromedriver.v2 as uc
import proxy_data
from time import sleep

PROXY = "185.239.140.165:49155"
EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\wp_importer\chromedriver.exe'


def set_driver(proxy_n):

    IP         = proxy_data.IP_LIST[proxy_n]
    HTTPS_PORT = proxy_data.HTTPS_PORT

    options = uc.ChromeOptions()
    options.add_argument(f'--proxy-server=http://{IP}:{HTTPS_PORT}')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    d = uc.Chrome(executable_path=EXECUTABLE_PATH, options=options)
    
    return d



d1 = set_driver(0)
d1.get('https://whatismyipaddress.com/')

d2 = set_driver(1)
d2.get('https://whatismyipaddress.com/')


sleep(1000)