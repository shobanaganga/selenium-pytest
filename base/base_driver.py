import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver


    def page_scroll(self):
        pagelength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight")
        match = False
        while (match == False):
            lastcount = pagelength
            time.sleep(3)
            pagelength = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight")
            time.sleep(2)
            if lastcount == pagelength:
                match = True
        time.sleep(4)

    def wait_for_element_to_be_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element

    def wait_for_presence_of_all_elements_located(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return element