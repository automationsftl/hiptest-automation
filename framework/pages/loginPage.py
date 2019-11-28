from selenium.common.exceptions import NoSuchElementException


class LoginPage(object):

    def __init__(self, webapp):
        self.__driver = webapp.driver

        self.username_input_id = "email"
        self.password_input_id = "password"
        self.login_button_xpath = ".//button[@type='submit']"
        self.login_url = "https://op-apclassroom-content.collegeboard.org/login?directlogin=true"

    def enter_username(self, username):
        username_input = self.__driver.find_element_by_id(self.username_input_id)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.__driver.find_element_by_id(self.password_input_id)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        self.__driver.find_element_by_xpath(self.login_button_xpath).click()

    def go_to(self):
        self.__driver.get(self.login_url)

    def invalid_login(self):
        try:
            # find_element_by_xpath throws an NoSuchElementException in case the element is not found.
            # If home image is found we return True, otherwise it returns False in case of NoSuchElementException
            self.__driver.find_element_by_xpath(".//li[text()='Invalid username or password']")
            return True
        except NoSuchElementException:
            return False