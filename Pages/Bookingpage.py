import logging
import time
from Pages.Basepage import Basepage
from Pages.Logger_setup import setup_logger
from misc import create_popup


class Booking(Basepage):
    def __init__(self,driver):
        super().__init__(driver)
        setup_logger(log_file='myclass.log', log_level=logging.INFO)

    flight_linktext = "Flights"

    def click_button(self):
        entered_value = create_popup()
        logging.info("Value entered in the popup: %s", entered_value)
        time.sleep(10)
        self.click_a_element("flight_linktext",self.flight_linktext)
        logging.info("Stared buddy")