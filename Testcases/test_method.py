from Pages.Bookingpage import Booking
from Testcases.Basetest import BaseTest


class Test_Website(BaseTest):
    def test_function1(self):
        function = Booking(self.driver)
        function.click_button()

