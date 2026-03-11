from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class PreCreditLocator(BaseLocator):

    card_type_dropdown = (By.XPATH, "//td[@field='%s']//a")
    card_type_select = (By.XPATH, "(//div[contains(text(), '%s')])[last()]")
    input_precredit_label = (By.XPATH, "(//td[@field='%s']//input)[last()-1]")
    text_precredit_label = (By.XPATH, "(//td[@field='%s']//div)[last()]")
    btn_add_precredit = (By.XPATH, "//span[@class='button-add--s']")
    btn_delete = (By.XPATH, "(//td[@field='modifyButton']//span)[last()]")
