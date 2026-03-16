from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class CheckinLocator(BaseLocator):

    btn_dialog_checkin = (By.XPATH, "//button[@data-field-id='r_1011']")
