import logging
import time
from selenium.webdriver.support.ui import Select
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Basepage import Basepage
from Pages.Logger_setup import setup_logger
from misc import create_popup


class Booking(Basepage):
    def __init__(self,driver):
        super().__init__(driver)
        setup_logger(log_file='myclass.log', log_level=logging.INFO)

    flight_linktext = "Flights"
    from_xpath = "//label[@for='fromCity']"
    to_xpath = "//label[@for='toCity']"
    from_input_xpath = "//input[@placeholder='From']"
    to_input_xpath = "//input[@placeholder='To']"
    departure_xpath = "//label[@for='departure']"
    return_xpath = "//div[@data-cy='returnArea']"
    classes_xpath = "//label[@for='travellers']"
    adult_link_xpath = "(//button[@class='addTravellerBtn'])[1]"
    adult_xpath = "//li[@data-cy='adults-1']"
    children_xpath = "//li[@data-cy='children-1']"
    apply_xpath = "//button[text()='APPLY']"
    search_xpath = "//a[text()='Search']"
    next_xpath = "//div[@class='scrollTopTrigger']"
    price_btn_xpath = "(//button[@class='ViewFareBtn  text-uppercase  clusterBtn'])[1]"
    final_price_xpath = "(// button[text() = 'BOOK NOW'])[1]"
    continue_xpath = "//button[text()='Continue']"
    mobile_no_xpath = "//input[@placeholder='Mobile No']"
    email_xpath = "//input[@placeholder='Email']"
    country_drop_xpath = "//input[@class='dropdownFieldWpr__input  ']"
    check_box_xpath = "//p[@data-cy='dt_cb_label_gst_info']"
    trip_secure_xpath = "(//input[@type='radio'])[5]"
    non_veg_xpath = "//input[@id='NON_VEG']"
    non_veg_item_xpath = "(//button[@class='mealAddBtn'])[1]"
    proceed_xpath = "//button[text()='Proceed to pay']"

    def click_button(self):
        logging.info(" ######################  STARTS HERE  ######################### ")
        logging.info("Stared buddy")
        # entered_value = create_popup()
        # logging.info("Value entered in the popup: %s", entered_value)
        self.click_a_element("flight_linktext",self.flight_linktext)

    def from_button(self):
        from_value = "Chennai"
        logging.info("Selecting the from place")
        time.sleep(2)
        self.wait_click_a_element("from_xpath", self.from_xpath,10)
        self.drop_down("from_input_xpath", self.from_input_xpath,from_value,1)
        logging.info("From place selected %s",str(from_value))

    def to_button(self):
        to_place = "Coimbatore"
        logging.info("Selecting the To place")
        self.click_a_element("to_xpath", self.to_xpath)
        self.drop_down("to_input_xpath", self.to_input_xpath,to_place,1)
        logging.info("To place selected %s", to_place)

    def from_date(self):
        # Eg format of the giving the month and date (Case sensitive)
        from_xpath = "//div[contains(@aria-label, 'Feb 25')]"
        logging.info("Selecting the departure date")
        # self.click_a_element("departure_xpath",self.departure_xpath)
        self.wait_click_a_element("from_xpath",from_xpath,2)
        logging.info("departure date selected")

    def to_date(self):
        to_xpath = "//div[contains(@aria-label,'Feb 20')]"
        logging.info("Selecting the return date")
        self.wait_click_a_element("return_xpath",self.return_xpath,5)
        self.wait_click_a_element("to_xpath",to_xpath,2)
        logging.info("return date selected")

    def adult_selection(self):
        self.wait_click_a_element("classes_xpath",self.classes_xpath,3)
        self.click_a_element("adult_xpath",self.adult_xpath)
        self.click_a_element("children_xpath", self.children_xpath)
        self.click_a_element("apply_xpath", self.apply_xpath)
        self.click_a_element("search_xpath", self.search_xpath)

    def price_select(self):
        try:
            alert_type = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"//button[text()='OKAY, GOT IT!']")))
            logging.info("Alert accepted")
            alert_type.click()
        except Exception as e:
            logging.error("An error occurred while handling the alert: %s", str(e))
        finally:
            logging.info("price selection begins")
            element = self.driver.find_element(By.XPATH, "//div[@class='textRight flexOne']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            # time.sleep(3000)
            price_tags = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='textRight flexOne']"))
            )
            raw_prices = [price.text.split("per")[0].split()[-1] for price in price_tags]
            logging.info(raw_prices)
            prices_int = [int(price.replace(",", "").replace("₹", "")) for price in raw_prices]
            logging.info(prices_int)
            sorted_prices = sorted(prices_int)
            logging.info(sorted_prices)
            lowest_index = prices_int.index(sorted_prices[0])
            logging.info(lowest_index)
            index = str(lowest_index)
            # price_btn_xpath = "(//div[@class='textRight flexOne']/following-sibling::button)["+index+"]"

    def click_a_price(self):
        logging.info("clicking a price")
        element = self.driver.find_element(By.XPATH, "(//button[@class='ViewFareBtn  text-uppercase  clusterBtn'])[3]")
        self.driver.execute_script("arguments[0].click();", element)
        logging.info("price button clicked")
        logging.info("selecting the last price")
        self.wait_click_a_element("final_price_xpath",self.final_price_xpath,20)
        logging.info("selected the last price")

    def enter_details(self):
        logging.info("entering details")
        new_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
        time.sleep(10)

    def trip_secure(self):
        logging.info("checking for trip secure")
        try:
            self.wait_click_a_element("trip_secure_xpath",self.trip_secure_xpath,20)
            logging.info("trip secure is available and clicked")
        except NoSuchElementException:
            print("Radio button not found. Continuing with remaining code...")
            logging.info("sorry. trip secure is not available")
        time.sleep(4)

    def adult_details(self):
        logging.info("Entering adults details")
        logging.info("clicking the  adult link")
        self.action_chains_click("adult_link_xpath",self.adult_link_xpath)
        logging.info("adult link clicked")
        name_xpath = "(//input[@placeholder='First & Middle Name'])[1]"
        self.enter_a_value("name_xpath",name_xpath,"Satis")
        lastname_xpath = "(//input[@placeholder='Last Name'])[1]"
        self.enter_a_value("lastname_xpath",lastname_xpath,"Kumar")
        male_xpath = "(//input[@value='MALE'])[1]"
        self.click_a_element("male_xpath",male_xpath)
        phone_xpath = "//input[@placeholder='Mobile No(Optional)']"
        self.enter_a_value("phone_xpath",phone_xpath,"8778164504")

        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, " (//div[@class='dropdown__control css-yk16xz-control'])[1]")))
        element.click()
        country_code_xpath ="//div[@class='dropdown__single-value css-1uccc91-singleValue']"
        self.wait_click_a_element("country_code_xpath",country_code_xpath,10)
        logging.info("adults details entered")

    def child_details(self):
        logging.info("Entering child details")
        logging.info("clicking the  adult link")
        adult_xpath = "(//button[@class='addTravellerBtn'])[2]"
        self.wait_click_a_element("adult_xpath", adult_xpath, 30)
        logging.info("adult link clicked")
        name_xpath = "(//input[@placeholder='First & Middle Name'])[2]"
        self.enter_a_value("name_xpath", name_xpath, "priya")
        lastname_xpath = "(//input[@placeholder='Last Name'])[2]"
        self.enter_a_value("lastname_xpath", lastname_xpath, "kumari")
        male_xpath = "(//input[@value='MALE'])[2]"
        self.click_a_element("male_xpath", male_xpath)
        logging.info("Entered child details")

        scroll_view_xpath = "(// div[@class ='appendRight10'])[3]"
        self.scroll_into_view("scroll_view_xpath",scroll_view_xpath,60)

        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, " (//div[@class='dropdown__control css-yk16xz-control'])[2]")))
        element.click()
        self.actions.send_keys(Keys.ARROW_DOWN * 0).perform()
        self.actions.send_keys(Keys.ENTER).perform()

        mobile_no_xpath = "//input[@placeholder='Mobile No']"
        self.javascript_click_send_keys("mobile_no_xpath",mobile_no_xpath,"8778164504",60)
        logging.info("entered mobile number")

        self.enter_a_value("email_xpath",self.email_xpath,"sksathis2002@gmail.com")
        logging.info("entered email")

        logging.info("checkbox will be selected")
        checkbox_xpath = "//p[@data-cy='dt_cb_label_gst_info']"
        self.scroll_into_view_click("checkbox_xpath",checkbox_xpath,60)
        logging.info("checkbox selected")

    def continue_btn(self):
        time.sleep(1)
        logging.info("Clicking continue button")
        element = self.driver.find_element(By.XPATH, "//button[text()='Continue']")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        logging.info("Continue btn clicked")

    def confirm_btn(self):
        logging.info("Confirm btn clicking")
        confirm_xpath = "//button[text()='CONFIRM']"
        self.wait_click_a_element("confirm_xpath",confirm_xpath,30)
        logging.info("Confirm btn clicked")

    def selecting_seat(self):
        logging.info("popup selecting")
        seat_value_xpath = "//button[text()='Yes, Please']"
        self.wait_click_a_element("seat_value_xpath",seat_value_xpath,30)
        logging.info("popup selected")
        time.sleep(5)
        logging.info("Continue2 btn clicking")
        confirm_xpath = "//button[text()='Continue']"
        self.wait_click_a_element("confirm_xpath", confirm_xpath, 30)
        logging.info("Continue2 btn clicked")

    def selection_food(self):
        time.sleep(1)
        logging.info("clicking non-veg")
        non_veg_xpath = "//input[@id='NON_VEG']"
        self.javascript_click("non_veg_xpath",non_veg_xpath,60)
        logging.info("clicked non-veg")
        logging.info("clicking non-veg item")
        non_veg_item_xpath = "(//button[text()='Add'])[1]"
        self.javascript_click("non_veg_item_xpath",non_veg_item_xpath,60)
        logging.info("clicking non-veg item")
        time.sleep(3)
        logging.info("clicking continue")
        self.wait_click_a_element("continue_xpath",self.continue_xpath,30)
        logging.info("clicking continue")

    def payment_method(self):
        logging.info("clicking proceed to pay")
        self.wait_click_a_element("proceed_xpath",self.proceed_xpath,30)
        logging.info("clicking proceed to pay")
        time.sleep(20)

# "//button[text()='Proceed to pay']"
# //input[@id='NON_VEG']
# (//button[text()='Add'])[1]