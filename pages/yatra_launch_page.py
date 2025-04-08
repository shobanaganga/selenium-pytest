from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class LaunchPage(BaseDriver):

    log = Utils.custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    DEPART_FROM = '//p[normalize-space()="Departure From"]'
    DEPART_FROM_FIELD = 'input-with-icon-adornment'
    DEPART_FROM_RESULT_LIST = '//div[@class="MuiBox-root css-134xwrj"]//div[@class="fw-600 mb-0"]'
    GOING_TO = '//p[normalize-space()="Going To"]'
    GOING_TO_FIELD = 'input-with-icon-adornment'
    GOING_TO_RESULT_LIST = '//div[@class="MuiStack-root css-1187icl"]//div[@class="fw-600 mb-0"]'
    DEPART_DATE = '(//div[@class="css-w7k25o"])[1]'
    DEPART_DATE_RESULT_LIST = '//div[@class="react-datepicker__month-container"]//div[@aria-label="month  2025-04"]//span[1]'
    SEARCH_BUTTON = '//button[normalize-space()="Search"]'

    def getDepartFrom(self):
        depart_from = self.wait_for_element_to_be_clickable(By.XPATH, self.DEPART_FROM)
        self.log.info("STEP 1 : Clicking on Depart From Auto Suggestion Text Field")
        depart_from.click()
        return self.driver.find_element(by=By.ID, value='input-with-icon-adornment')

    def getDepartFromResults(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.DEPART_FROM_RESULT_LIST)

    def enterDepartFromLocation(self,departfromlocation):
        depart_location = self.getDepartFrom()
        self.log.info("STEP 2 : Type Depart From Location {}".format(departfromlocation))
        depart_location.send_keys(departfromlocation)
        depart_search_list = self.getDepartFromResults()
        self.log.info('STEP 3 : Select {} from auto suggestion drop down'.format(departfromlocation))
        for depart in depart_search_list:
            if depart.text == "New Delhi, (DEL)":
                depart.click()
                break

    def getGoingTo(self):
        self.log.info("STEP 4 : Clicking on Going To Auto Suggestion Text Field")
        going_to = self.wait_for_element_to_be_clickable(By.XPATH,self.GOING_TO)
        going_to.click()
        return self.driver.find_element(by=By.ID,value=self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.GOING_TO_RESULT_LIST)

    def enterGoingToLocation(self,goingtolocation):
        going_location = self.getGoingTo()
        self.log.info("STEP 5 : Type Going To Location {}".format(goingtolocation))
        going_location.send_keys(goingtolocation)
        going_search_list = self.getGoingToResults()
        self.log.info('STEP 6 : Select {} from auto suggestion drop down'.format(goingtolocation))
        for going in going_search_list:
            if going.text == "Mumbai, (BOM)":
                going.click()
                break
    def getDepartDate(self):

        return self.wait_for_element_to_be_clickable(By.XPATH,self.DEPART_DATE)

    def getDepartDateResults(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.DEPART_DATE_RESULT_LIST)

    def enterDepartDate(self,departuredate):
        depart_date = self.getDepartDate()
        self.log.info('STEP 7 : Click on Departure Date Field')

        depart_date.click()
        all_dates = self.getDepartDateResults()
        for dates in all_dates:
            if dates.text == departuredate:
                self.log.info('STEP 8 : Select Departure Date')
                dates.click()
                break

    def click_search(self):
        self.log.info('STEP 9 : click Search')
        search_button = self.wait_for_element_to_be_clickable(By.XPATH,self.SEARCH_BUTTON)
        search_button.click()

    def searchflights(self,departfromlocation,goingtolocation,departuredate):
        self.enterDepartFromLocation(departfromlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartDate(departuredate)
        self.click_search()