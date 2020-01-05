from selenium.common.exceptions import NoSuchElementException


class ProgressCheckPage(object):
    def __init__(self, webapp):
        self.__driver = webapp.driver
        self.progress_check_xpath = ".//div[@class='PrimaryNav']//a[@class='active' and text()=\" assessments/assign\"]"

    def click_assign_button(self,position):
        button_xpath = ".//div[@class='action_buttons']//button[text()='Assign']"
        self.__driver.find_elements_by_xpath(button_xpath)[position].click()

    def get_title(self, position):
        title_elements = self.__driver.find_elements_by_xpath(".//tbody//div[@class='rich_title_wrapper']")
        title_element = title_elements[position]
        return title_element.text

    def is_valid_popup(self, title):
        # title_xpath = ".//div[@class='Modal']//div[text()='Unit 1 Progress Check: MCQ Part B']"
        title_xpath = ".//div[@class='Modal']//div[text()= '" + title + "']"
        try:
            self.__driver.find_element_by_xpath(title_xpath)
            return True
        except NoSuchElementException:
            return False


    def is_progress_check(self):
        try:
            self.__driver.find_element_by_xpath(self.progress_check_xpath)
            return True
        except NoSuchElementException:
            return False