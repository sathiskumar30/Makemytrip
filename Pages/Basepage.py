from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class Basepage:
    def __init__(self,driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID,locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_classname"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css_selector"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_by_strategy(self, locator_name):
        if locator_name.endswith("_id"):
            return By.ID
        elif locator_name.endswith("_name"):
            return By.NAME
        elif locator_name.endswith("_classname"):
            return By.CLASS_NAME
        elif locator_name.endswith("_linktext"):
            return By.LINK_TEXT
        elif locator_name.endswith("_xpath"):
            return By.XPATH
        elif locator_name.endswith("_css_selector"):
            return By.CSS_SELECTOR
        else:
            raise ValueError(f"Unsupported locator_name: {locator_name}")

    def wait_for_element(self, by_strategy, locator_value, timeout):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by_strategy, locator_value))
            )
            print("Element located successfully:", timeout)
            return element

        except Exception as e:
            print(f"Error: {e}")

    def wait_click_a_element(self, locator_name, locator_value ,value):
        by_strategy = self.get_by_strategy(locator_name)
        element = self.wait_for_element(by_strategy, locator_value,value)
        print("Clicking the element:", element)
        element.click()

    def wait_enter_a_value(self,locator_name,locator_value,name,value):
        by_strategy = self.get_by_strategy(locator_name)
        element = self.wait_for_element(by_strategy, locator_value,value)
        element.click()
        element.clear()
        element.send_keys(name)

    def click_a_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def enter_a_value(self,locator_name,locator_value,value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(value)

    def drop_down(self, locator_name, locator_value, value,drop_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((self.get_by_strategy(locator_name), locator_value))
            )
            element.send_keys(value)
            time.sleep(2)
            self.actions.send_keys(Keys.ARROW_DOWN * drop_value).perform()
            self.actions.send_keys(Keys.ENTER).perform()

        except Exception as e:
            print(f"Error: {e}")

    def date(self,locator_name, locator_value ,date):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(date)
        element.send_keys(Keys.RETURN)


