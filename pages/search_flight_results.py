from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from utilities.utils import Utils

class SearchFlightsResults(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    FILTER_BY_NON_STOPS = '//p[normalize-space()="0"]'
    FILTER_BY_1_STOPS = '//p[normalize-space()="1"]'
    FILTER_BY_2_STOPS = '//p[normalize-space()="2"]'
    SEARCH_FLIGHT_RESULTS = '(//span[contains(text(),"Non Stop") or contains(text(),"1 Stop") or contains(text(),"2 Stop")])'

    def get_filter_by_non_stops(self):
        self.log.debug('STEP 10 : Filter 0 stops')
        return self.wait_for_element_to_be_clickable(By.XPATH,self.FILTER_BY_NON_STOPS)

    def get_filter_by_1_stops(self):
        self.log.info('STEP 10 : Filter 1 stops')
        return self.wait_for_element_to_be_clickable(By.XPATH,self.FILTER_BY_1_STOPS)

    def get_filter_by_2_stops(self):
        self.log.info('STEP 10 : Filter 2 stops')
        stop_2 =  self.wait_for_element_to_be_clickable(By.XPATH,self.FILTER_BY_2_STOPS)
        if stop_2.is_enabled():
            return stop_2

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.SEARCH_FLIGHT_RESULTS)

    def filter_stops(self,by_stop):
        if by_stop == "Non Stop":
            stop = self.get_filter_by_non_stops()
            stop.click()

        elif by_stop == "1 Stop":
            stop = self.get_filter_by_1_stops()
            stop.click()

        elif by_stop == "2 Stop":
            if self.stop:
                stop = self.get_filter_by_2_stops()
                stop.click()
            else:
                print("No flights available")

        else:
            print("Please provide valid stops")




