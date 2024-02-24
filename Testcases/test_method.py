import time
from Pages.Bookingpage import Booking
from Testcases.Basetest import BaseTest


class Test_Website(BaseTest):
    def test_function1(self):
        function = Booking(self.driver)
        function.click_button()
        function.from_button()
        function.to_button()
        function.from_date()
        function.adult_selection()
        function.price_select()
        function.click_a_price()
        function.enter_details()
        function.trip_secure()
        function.adult_details()
        function.child_details()
        function.continue_btn()
        function.confirm_btn()
        function.selecting_seat()
        function.selection_food()
        function.payment_method()


