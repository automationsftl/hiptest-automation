from selenium.common.exceptions import NoSuchElementException


class PPC(object):
    def __init__(self, webapp):
        self.__driver = webapp.driver
        self.progress_check_xpath = ".//div[@class='PrimaryNav']//a[@class='active' and text()='Progress Checks']"

    def navigate_to_progress_check(self):
        progress_xpath = ".//a[contains(@href, '/assessments/assign')]"
        self.__driver.find_element_by_xpath(progress_xpath).click()
