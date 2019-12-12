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

    def select_unit_tab(self):
        units = self.__driver.find_elements_by_xpath(".//div[@class='unitsWidget']//div[contains(@class, 'ResponsiveTabs--items')]//a[@role='button']")
        index = int(len(units)/2)

        self.__driver.execute_script("arguments[0].scrollIntoView();", units[index])
        units[index].click()

        return units[index].text

    def navigate_to_dashboard(self):
        dashboard_xpath = ".//a[contains(@href, '/dashboard')]"
        self.__driver.find_element_by_xpath(dashboard_xpath).click()

    def navigate_to_progress_check(self):
        progress_xpath = ".//a[contains(@href, '/assessments/assign')]"
        self.__driver.find_element_by_xpath(progress_xpath).click()

    def navigate_to_homePage(self):
        home_xpath = ".//a[contains(@href, '/home')]"
        self.__driver.find_element_by_xpath(home_xpath).click()

    def get_selected_unit(self):
        selected_unit_xpath = ".//div[contains(@class, 'ResponsiveTabs--item is-selected')]"

        selected_unit = self.__driver.find_element_by_xpath(selected_unit_xpath)
        return selected_unit.text

    def click_assign_button(self, position):
        button_xpath = ".//div[@class='action_buttons']//button[text()='Assign']"
        self.__driver.find_elements_by_xpath(button_xpath)[position].click()

    def get_title(self, position):
        title_elements = self.__driver.find_elements_by_xpath(".//tbody//div[@class='rich_title_wrapper']")
        title_element = title_elements[position]

        return title_element.text

    def is_valid_popup(self, title):

        # title_xpath = ".//div[@class='Modal']//div[text()= 'Unit 1 Progress Check: MCQ Part A']"
        title_xpath = ".//div[@class='Modal']//div[text()= '" + title + "']"

        try:
            self.__driver.find_element_by_xpath(title_xpath)
            return True
        except NoSuchElementException:
            return False











