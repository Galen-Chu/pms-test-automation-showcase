from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class SparePartsBatchLocator(BaseLocator):

    batch_spare_dropdown = (By.XPATH, "//div[@data-field-id='itemCode']")
    batch_spare_options = (By.XPATH, "//ul[@id='itemCode_options']//span[text()='%s']")
    input_batch_spare_by_label = (By.XPATH, "//input[@id='%s']")
    text_batch_spare_by_label = (By.XPATH, "//td[@field='%s']")
    btn_batch_spare = (
        By.XPATH,
        "//div[text()='備品批次新增']/ancestor::div//button[@title='儲存']",
    )
    btn_save_batch_spare = (By.XPATH, "(//div[@data-field-id='save'])[last()]")
    checkbox_guest = (By.XPATH, "(//span[contains(@class, 'e-uncheck')])[last()]")
