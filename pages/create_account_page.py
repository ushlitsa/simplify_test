import time
class CreateAcc():


    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)


    def filling_fields(self,user_dictionary):
        first_name_field = self.driver.find_element_by_id("firstName")
        last_name_field = self.driver.find_element_by_id("lastName")
        password_field = self.driver.find_element_by_name("Passwd")
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")

        first_name_field.send_keys(user_dictionary['fn'])
        last_name_field.send_keys(user_dictionary['ln'])
        password_field.send_keys(user_dictionary['password'])
        confirm_password_field.send_keys(user_dictionary['password'])

    def validation(self,validation_error,email_list):
        username_field = self.driver.find_element_by_id("username")
        next_button = self.driver.find_element_by_id("accountDetailsNext")
        for email in email_list:
            username_field.clear()
            username_field.send_keys(email)
            next_button.click()
            assert validation_error not in self.driver.page_source
            time.sleep(1)