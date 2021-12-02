from selenium import webdriver
from time import sleep

# COOKIES_FOLDER = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\git_folder\walla_bot\cookies_folder'
# #v96
# EXECUTABLE_PATH = r'C:\Users\HP EliteBook\OneDrive\A_Miscalaneus\Escritorio\Code\chromedriver.exe'

#OVERVIEW
#user logins in, program asks for name and save the cookies with the input name

#STEPS
#start new walla driver
#human logins in manually
#ask input: cookies_file_name, human inputs the email
#program saves those cookies with walla_email.pkl
# repeat 


# def save_cookies(d, COOKIES_FILENAME_MAIL):
#     ''' d, COOKIES_FILE // if COOKIES_FILE name not specified = cookies_last_login.pkl '''
#     import pickle
    
#     COOKIES_FILE_PATH = COOKIES_FOLDER + '\\' + COOKIES_FILENAME_MAIL+ '.pkl'
#     with open(COOKIES_FILE_PATH, "wb") as f:
#         pickle.dump( d.get_cookies(), f)


def run():
    url = input('pon aqui la url a la que quieres ir y pulsa enter: ')
    for _ in range(100):
        import undetected_chromedriver.v2 as uc

        options = uc.ChromeOptions()
        # d = uc.Chrome(executable_path=EXECUTABLE_PATH,options=options)
        d = uc.Chrome(options=options)
        d.get(url)

        #close 1º window
        if len(d.window_handles) != 1:
            first_winodw = d.window_handles[0]
            second_winodw = d.window_handles[1]
            
            d.switch_to.window(first_winodw)
            d.close()
            sleep(2)
            d.switch_to.window(second_winodw)

        again = input('pulsa enter para lanzar un nuevo driver o cierra esta pantalla para terminar la sesión')
        # filename = 'walla_'+mail
        # save_cookies(d, filename)


if __name__ == '__main__':
    run()
