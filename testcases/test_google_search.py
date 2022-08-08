import os
import pytest
import softest
from pages.google_search_page import Google_Search_Home_Page
from utilities.utilities_page import Utilities
os.environ['GH_TOKEN'] = "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"


from ddt import ddt, file_data, data, unpack
@pytest.mark.usefixtures("setup")
@ddt

class TestGoogleSearch(softest.TestCase):
    log = Utilities.custom_logger()

    @data(*Utilities.read_file_csv("C:\\Users\\nobit\\OneDrive\\Desktop\\googleSearchFlight\\testdatas\\tdatacsv.csv"))
    #4 @data(*Utilities.read_excel_file("C:\\Users\\nobit\\OneDrive\\Desktop\\googleSearchFlight\\testdatas\\tdataexcel.xlsx","Sheet1"))
    #3 #@file_data("../testdata/testyml.yaml")
    #2 #@file_data("../testdata/testdata.json")
    #1 #@data(("Los", "Calgary", "2022-11-23", "1 stop"))
    @unpack
    def test_google_search(self, goingfrom, goingto, date, stops):
        self.log.info("go to google search home page")
        self.gs1 = Google_Search_Home_Page(self.driver)
        self.log.info("go to google search flight result")
        gs2 = self.gs1.function_google_search_home_page(goingfrom, goingto, date)
        gs2.google_search_2()
        list_assertion = gs2.list_results_flights()
        ut = Utilities()
        ut.assertion_value_flights(list_assertion, stops)


