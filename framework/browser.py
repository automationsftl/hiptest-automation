from selenium import webdriver

class WebApp(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
