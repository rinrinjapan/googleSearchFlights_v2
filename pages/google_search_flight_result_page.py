import time
from selenium.webdriver.common.by import By
from base.base_page import BaseGoogleSearch
from utilities.utilities_page import Utilities

class Google_Search_Result_Page(BaseGoogleSearch):

    log = Utilities.custom_logger()

    def __init__(self, driver):
        self.driver = driver


    #1. click general stops
    click_on_stops = "//button[@aria-label= 'Stops, Not selected']"
    def click_on_stops_pop_up(self):
        return self.base_element_to_be_clickable(By.XPATH, self.click_on_stops)


    #2. click on 2 stop or a few
    click_2_stops = "//input[@aria-label='2 stops or fewer']"
    def click_2_stops_pop_up(self):
        return self.driver.find_element(By.XPATH, self.click_2_stops)


    #3. click on Non-stop
    click_non_stop = "//input[@aria-label='Nonstop only']"
    def click_non_stop_pop_up(self):
        return self.driver.find_element(By.XPATH, self.click_non_stop)


    #4. click any stop
    click_any_stop = "//input[@aria-label='Any number of stops']"
    def click_any_stop_pop_up(self):
        return self.driver.find_element(By.XPATH, self.click_any_stop)


    #5. click on 1 stop or a few
    click_1_stop = "//input[@aria-label='1 stop or fewer']"
    def click_1_stop_pop_up(self):
        return self.driver.find_element(By.XPATH, self.click_1_stop)


    #6. click on "clear on Stop"
    click_on_clear = "//span[text()='Clear']"
    def click_on_clear_pop_up(self):
        return self.driver.find_element(By.XPATH, self.click_on_clear)


    #7. click on "close dialog" in stop
    click_on_close = "//div[@jsname='M7dhxe']//button[@aria-label='Close dialog']"
    def click_on_close_pop_up(self):
        return self.driver.find_element(By.XPATH, self.click_on_close)


    #8. click on "view more"
    click_more_flights = "//li[@class='ZVk93d']//button"
    def click_more_flights_pop_up(self):
        return self.driver.find_element(By.XPATH, self.click_more_flights)


    #asertion result
    list_of_places = "//span[contains(text(), 'Nonstop') or contains(text(),'1 stop') or contains(text(),'2 stops')]"
    def list_results_flights(self):
        return self.driver.find_elements(By.XPATH, self.list_of_places)


    def google_search_2(self):
        # click search on how many stops
        self.log.info("Click on stops button")
        self.click_on_stops_pop_up().click()
        time.sleep(3)

        # 2 stop or a few
        self.log.info("click on 2 stops searching")
        self.click_2_stops_pop_up().click()
        time.sleep(4)

        # Non-stop
        self.log.info("click on non stop searching")
        self.click_non_stop_pop_up().click()
        time.sleep(3)

        # any stop
        self.log.info("click on any stops searching")
        self.click_any_stop_pop_up().click()
        time.sleep(3)

        # 1 stop or a few
        self.log.info("click on 1 stop searching")
        self.click_1_stop_pop_up().click()
        time.sleep(3)

        # clear on Stop
        self.log.info("click on clear stop")
        self.click_on_clear_pop_up().click()
        time.sleep(3)

        # close dialog tren stop
        self.log.info("click on close pop -up")
        self.click_on_close_pop_up().click()
        time.sleep(3)

        # view more
        self.log.info("we are going to see more flights yeah")
        self.click_more_flights_pop_up().click()
        time.sleep(10)


    def filter_stops(self, by_stop):

        if by_stop == "2 stops":
            self.log.info("clicked on button stop")
            self.click_on_stops_pop_up().click()
            time.sleep(2)
            self.log.info("selected flights with 2 stops")
            self.click_2_stops_pop_up().click()
            time.sleep(2)

        elif by_stop == "1 stop":
            self.log.info("clicked on button stop")
            self.click_on_stops_pop_up().click()
            time.sleep(2)
            self.log.info("selected flights with 1 stop")
            self.click_1_stop_pop_up().click()
            time.sleep(2)
            # clear on Stop
            self.log.info("click on clear stop")
            self.click_on_clear_pop_up().click()
            time.sleep(2)
            # close dialog tren stop
            self.log.info("click on close pop-up")
            self.click_on_close_pop_up().click()
            time.sleep(2)

        elif by_stop == "non stop":
            self.log.info("clicked on button stop")
            self.click_on_stops_pop_up().click()
            time.sleep(2)
            self.log.info("selected flights non-stop")
            self.click_non_stop_pop_up().click()
            time.sleep(2)

        elif by_stop == "any stop":
            self.log.info("clicked on button stop")
            self.click_on_stops_pop_up().click()
            time.sleep(2)
            self.log.info("selected flights with any stop")
            self.click_any_stop_pop_up().click()
            time.sleep(2)

        else:
            self.log.warning("provide a valid stop")

        # view more
        self.log.info("we are going to see more flights yeah")
        self.click_more_flights_pop_up().click()
        time.sleep(10)





