import pytest
import softest
from pages.search_flight_results import SearchFlightsResults
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt,data,unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):

    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.sf = SearchFlightsResults(self.driver)
        self.ut = Utils()
    @data(("New Delhi","Mumbai","17","Non Stop"),("New Delhi","Mumbai","17","1 Stop"))
    @unpack
    def test_search_flights_non_stop(self,departfrom,goingto,date,stop):
        self.log.info("TEST CASE STARTED: FILTER {} FLIGHTS".format(stop))
        self.lp.searchflights(departfrom,goingto,date)
        self.lp.page_scroll()
        self.sf.filter_stops(stop)
        all_1_stops = self.sf.get_search_flight_results()
        self.ut.assert_list_item(all_1_stops,stop)
        self.log.info("TEST CASE ENDED: FILTER {} FLIGHTS".format(stop
                                                                  ))


    #def test_search_flights_1_stop(self):
        #self.log.info("TEST CASE STARTED: FILTER 1 STOP FLIGHTS")
        #self.lp.searchflights("New Delhi","Mumbai","17")
        #self.lp.page_scroll()
        #self.sf.filter_stops("1 Stop")
        #all_1_stops = self.sf.get_search_flight_results()
        #self.ut.assert_list_item(all_1_stops,"1 Stop")
        #self.log.info("TEST CASE ENDED: FILTER 1 STOP FLIGHTS")




