from selenium import webdriver
import time
from pages.sign_in_page import SignIn
from pages.create_account_page import CreateAcc


driver = webdriver.Chrome('E:/Studying/QAA/1/chromedriver_win32/chromedriver')
driver.implicitly_wait(5)
driver.get("https://accounts.google.com")


my_sign_in = SignIn(driver)
my_sign_in.create_account()


validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}
user_dictionary = {'fn':'Alex', 'ln':'Kardash', 'password': 'Abc123456!'}


my_create_acc = CreateAcc(driver)
my_create_acc.filling_fields(user_dictionary)
my_create_acc.validation(validation_error,email_list)


driver.quit()