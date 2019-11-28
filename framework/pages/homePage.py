from selenium.common.exceptions import NoSuchElementException


class HomePage(object):
    def __init__(self, webapp):
        self.__driver = webapp.driver
        self.single_subject_home_xpath = ".//div[@class='PrimaryNav']//a[@class='active' and text()=\" Home\"]"

    def is_homepage(self):
        try:
            # find_element_by_xpath throws an NoSuchElementException in case the element is not found.
            # If home image is found we return True, otherwise it returns False in case of NoSuchElementException
            self.__driver.find_element_by_xpath(self.single_subject_home_xpath)
            return True
        except NoSuchElementException:
            return False

    def has_subject(self, subject):
        try:
            # .//span[@class="subsel__label" and text()="AP Calculus AB"]
            subject_xpath = ".//span[@class='subsel__label' and text()='" + subject + "']"

            self.__driver.find_element_by_xpath(subject_xpath)
            return True
        except NoSuchElementException:
            return False
