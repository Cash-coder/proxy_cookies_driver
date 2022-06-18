from selenium import webdriver
from proxy_login import set_driver #py file

COOKIES_FOLDER = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\login and launcher\cookies_folder'
#v96
EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\chromedriver.exe'

#OVERVIEW
#user logins in, program asks for name and save the cookies with the input name

#STEPS
#start new walla driver
#human logins in manually
#ask input: cookies_file_name, human inputs the email
#program saves those cookies with walla_email.pkl
# repeat 


def save_cookies(d, city):
    ''' d, COOKIES_FILE // if COOKIES_FILE name not specified = cookies_last_login.pkl '''
    import pickle
    
    COOKIES_FILE_PATH = COOKIES_FOLDER + '\\' + city + '.pkl'
    with open(COOKIES_FILE_PATH, "wb") as f:
        pickle.dump( d.get_cookies(), f)



def run():
    for i in range(30):
        # import undetected_chromedriver.v2 as uc
        # options = uc.ChromeOptions()
        # d = uc.Chrome(executable_path=EXECUTABLE_PATH,options=options)

        d, city = set_driver(i)

        d.get('https://es.wallapop.com/')

        try:
            continue_mark = input('Press enter to continue ')
            save_cookies(d, city)

        finally:
            d.delete_all_cookies()
            d.close()


if __name__ == '__main__':
    run()
