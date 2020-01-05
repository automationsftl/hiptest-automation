from selenium.common.exceptions import NoSuchElementException


class AppHeaderComponent(object):
    def __init__(self, webapp):
        self.__driver = webapp.driver

    def navigate_to_progress_check(self):
        progress_xpath = ".//a[contains(@href, '/assessments/assign')]"
        self.__driver.find_element_by_xpath(progress_xpath).click()

    def navigate_to_dashboard(self):
        dashboard_xpath = ".//a[contains(@href, '/dashboard')]"
        self.__driver.find_element_by_xpath(dashboard_xpath).click()

    def navigate_to_question_bank(self):
        question_bank_xpath = ".//a[contains(@href,'/question_bank/create')]"
        self.__driver.find_element_by_xpath(question_bank_xpath).click()

    def navigate_to_professional_learning(self):
        professional_learning_xpath = ".//a[contains(@href,'https://op-cb-content.collegeboard.org/n/auth/redirect/?next=https%3A%2F%2Fop-cb-content.collegeboard.org%2Fn%2Fpl%23%2Fcalculus&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzYzNTA2MTAsImlhdCI6MTU3NjM0NzAxMCwibmJmIjoxNTc2MzQ3MDEwLCJqdGkiOiJjYjY3MTBhNC02YjZjLTQ1NWEtOTM3Mi01YzlhY2U1OGZkOWEiLCJpZGVudGl0eSI6eyJhbV91c2VyX2lkIjo3MjAyMTQ1ODMsImltcG9ydF9pZCI6IjcyMDIxNDAwMCIsInVzZXJuYW1lIjoiTUFUUklYLlRlYWNoZXJAdGVzdHNjaG9vbC5vcmciLCJwcmVmZXJlbmNlcyI6e30sInBpbG90IjoicDJfMjAxOF8wOCJ9LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MiLCJ1c2VyX2NsYWltcyI6e319._0Qm7j5R1W4gxdZh3clAeJ_YaEgPzzHci7HWvdIWk50&refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk5Njc1ODQsImlhdCI6MTU3NjA3OTU4NCwibmJmIjoxNTc2MDc5NTg0LCJqdGkiOiI1NzBiNjNmOS03NmIyLTQyMzQtODBiOS0xN2YzNGZmNzk3NWEiLCJpZGVudGl0eSI6eyJhbV91c2VyX2lkIjo3MjAyMTQ1ODMsImltcG9ydF9pZCI6IjcyMDIxNDAwMCIsInVzZXJuYW1lIjoiTUFUUklYLlRlYWNoZXJAdGVzdHNjaG9vbC5vcmciLCJwcmVmZXJlbmNlcyI6e30sInBpbG90IjoicDJfMjAxOF8wOCJ9LCJ0eXBlIjoicmVmcmVzaCJ9.ssMFXcFVsYKX83rCF1m72ExJpgXhN61YPp7OnhbdNz0&expires=1576350610441')]"
        self.__driver.find_element_by_xpath(professional_learning_xpath).click()

    def navigate_to_my_classes(self):
        myclasses_xpath = ".//a[contains(@href,'https://amdev.apfym-nonprod.collegeboard.org/courses')]"
        self.__driver.find_element_by_xpath(myclasses_xpath).click()

