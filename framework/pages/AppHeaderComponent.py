class AppHeaderComponent(object):
    def __init__(self, webapp):
        self.__driver = webapp.driver
        self.single_subject_home_xpath = ".//div[@class='PrimaryNav']//a[@class='active' and text()=\" Home\"]"

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
        self.__driver.find_element_by_xpath(button_xpath)[position].click()

    def get_title(self , position):
        title_elements = self.__driver.find_element_by_xpath(".//tbody//div[@class='rich_title_wrapper']")
        title_element = title_elements[position]
        return title_element.text

    def is_valid_popup(self , title):
         try:

            title_xpath = ".//div[@class='Modal']//div[text()= '" + title + "']"

            self.__driver.find_element_by_xpath(title_xpath)
            return True
        except NoSuchElementException:
            return False

    def select_checkbox(self):
        checkbox_xpath = ".//div[@class='custom-checkbox']"
        self.__driver.find_element_by_xpath(checkbox_xpath).click()

    def select_toggle(self):
        toggle_xpath =

