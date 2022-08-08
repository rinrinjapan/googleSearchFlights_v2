import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseGoogleSearch():

    def __init__(self, driver):
        self.driver = driver


    def base_element_to_be_clickable(self, locator_type, locator):
        ex_wait = WebDriverWait(self.driver, 20)
        return ex_wait.until(EC.element_to_be_clickable((locator_type, locator)))


    def base_presence_of_all_elements_located(self, locator_type, locator):
        ex_wait = WebDriverWait(self.driver, 20)
        return ex_wait.until(EC.presence_of_all_elements_located((locator_type, locator)))


    def autoscroll_page(self):
        pagelength = self.driver.excute_script(
            "window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength; ")
        flag = False
        while flag == False:
            maxl = pagelength
            pagelength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength;")
            if maxl == pagelength:
                flag = True
        time.sleep(3)

