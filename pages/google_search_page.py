import time
from selenium.webdriver.common.by import By
from base.base_page import BaseGoogleSearch
from utilities.utilities_page import Utilities
from pages.google_search_flight_result_page import Google_Search_Result_Page
class Google_Search_Home_Page(BaseGoogleSearch):

    log = Utilities.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    #1.1  input departure step 1
    departure_field = "//input[@value='Calgary']"
    def click_departure_field(self):
        return self.base_element_to_be_clickable(By.XPATH, self.departure_field)

    #1.2 input departure step 2
    departure_field_send_keys = "//div[@aria-label='Enter your origin']//div//input[@aria-label='Where else?']"
    def send_keys_departure_field(self):
        return self.base_element_to_be_clickable(By.XPATH, self.departure_field_send_keys)

    #1.3 input departure step 3
    list_departure_field = "//ul[@class='DFGgtd']//li//div[@class='CwL3Ec']//div[@class='w1ZvBc']"
    def pick_up_departure(self, depart):
        list_departure = self.base_presence_of_all_elements_located(By.XPATH, self.list_departure_field)
        for place in list_departure:
            if depart in place.text:
                place.click()
                break
        time.sleep(2)


    #2.1 input arrival step 1
    arrival_field = "//div[@aria-placeholder= 'Where to?']//input[@placeholder='Where to?']"
    def click_arrival_field(self):
        return self.base_element_to_be_clickable(By.XPATH, self.arrival_field)

    #2.2 input arrival step 2
    arrival_field_send_key = "//div[@aria-label='Enter your destination']//input"
    def send_keys_arrival_field(self):
        return self.base_element_to_be_clickable(By.XPATH, self.arrival_field_send_key)

    # 2.3 input arrival step 3
    list_arrival_field = "//ul[@class='DFGgtd']//li//div[@class='zsRT0d']"
    def pick_up_arrival(self,depart):
        list_arrival = self.base_presence_of_all_elements_located(By.XPATH, self.list_arrival_field)
        time.sleep(2)
        for place in list_arrival:
            if depart in place.text:
                place.click()
                break


    #3.1 pickup way step 1
    choose_way = "//div[@data-hveid='CAEQBA']//div[@class='RLVa8 GeHXyb']"
    def click_choose_way(self):
        return self.base_element_to_be_clickable(By.XPATH, self.choose_way)

    # 3.2 pickup way step 2
    click_one_way = "//ul[@aria-label='Select your ticket type.'][@role='listbox']//li[2]"
    def click_choose_one_way(self):
        return self.base_element_to_be_clickable(By.XPATH, self.click_one_way)


    #4.1 input number of customer step 1
    number_passengers = "//div[@class='Hj7hq LLHSpd']"
    def click_number_passengers(self):
        return self.base_element_to_be_clickable(By.XPATH, self.number_passengers)

    #4.2 input number of customer step 2
    add_more_passenger = "div[id='i5-2'] span[aria-live='polite']+ span"
    def add_passengers(self):
        return self.base_element_to_be_clickable(By.CSS_SELECTOR, self.add_more_passenger)

    #4.3 input number of customer step 3
    done_passenger = "//div[@class='IUKzPc']//button[@jsname='McfNlf']"
    def click_done_passengers(self):
        return self.base_element_to_be_clickable(By.XPATH, self.done_passenger)


    #5.1 choose date step 1
    choose_date = "//div[@jsname='huwV5e']//input[@placeholder='Departure']"
    def choose_date_flight(self):
        return self.base_element_to_be_clickable(By.XPATH, self.choose_date)

    #5.2 choose date step 2
    list_dates = "//div[@class='SJyhnc bVf6m']//div[@role='rowgroup']//div[@jsname='mG3Az']"
    def choose_date_in_list(self):
        return self.base_presence_of_all_elements_located(By.XPATH, self.list_dates)

    #5.3 --> choose date step 3
    done_google_1 = "//div[@jsname='WCieBd']//span[@jsname='V67aGc']"
    def click_Done_transfer_to_google2(self):
        return self.base_element_to_be_clickable(By.XPATH, self.done_google_1)

    #---------------------------------------------------------------------------#

    #1. summarizing input departure
    def input_departure_f(self, depart):
        self.click_departure_field().click()
        self.send_keys_departure_field().send_keys(depart)
        time.sleep(2)
        self.pick_up_departure(depart)
        time.sleep(2)


    #2. sumarizing input arrival
    def input_arrival_f(self, arrive):
        self.click_arrival_field().click()
        self.send_keys_arrival_field().send_keys(arrive)
        time.sleep(2)
        self.pick_up_arrival(arrive)
        time.sleep(2)

    #3 pickup way
    def input_way_f(self):
        self.click_choose_way().click()
        self.click_choose_one_way().click()

    #4 pickup number of customers
    def input_cus_f(self):
        self.click_number_passengers().click()
        self.add_passengers().click()
        self.click_done_passengers().click()

    # 5 pickup date
    def input_date_f(self, datet):
        self.choose_date_flight().click()
        all_dates = self.choose_date_in_list()
        for date in all_dates:
            if date.get_attribute("data-iso") == datet:
                date.click()
                break

    # 6 click "Done" on google search page >> transfer to Google Search Result
    def transfer_to_search_result_page(self):
        self.click_Done_transfer_to_google2().click()
        search_result_page = Google_Search_Result_Page(self.driver)
        return search_result_page


    def function_google_search_home_page(self, goingfrom, goingto, date ):
        # 1 input departure
        self.log.info("select departure")
        self.input_departure_f(goingfrom)
        # 2 input arrival
        self.log.info("select arrival")
        self.input_arrival_f(goingto)
        # 3 pickup way
        self.log.info("pickup a way")
        self.input_way_f()
        # 4 input number of customer
        self.log.info("choose number customers")
        self.input_cus_f()
        # 5 choose date
        self.log.info("pick up a date")
        self.input_date_f(date)
        # 6 transfering google search result page
        self.log.info("transfering to google search result page")
        google_search_result = self.transfer_to_search_result_page()
        return google_search_result



