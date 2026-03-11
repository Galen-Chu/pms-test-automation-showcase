
from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class ServiceItemLocator(BaseLocator):
    # 新增服務項目視窗
    service_dropdown = (By.XPATH, "//div[./label[normalize-space()='%s']]//input[@type='text']")
    service_dropdown_list = (By.XPATH, "//div[.//text()='新增服務項目']/following::div//div[contains(text(), '%s')]")
    days_setting_column = (By.XPATH, "//div[.//text()='天數設定']//input[1]")
    btn_confirm_days_setting = (By.XPATH, "//div[.//text()='天數設定']//button[normalize-space()='確定']")
    weekday_dropdown = (By.XPATH, "//div[.//text()='天數設定']//div[contains(@class, 'multiselect')]")
    weekday_dropdown_list = (By.XPATH, "//li[.//text()='%s']")
    start_date_datetable = (By.XPATH, "//div[.//text()='新增服務項目']//following::tbody[1]//span[normalize-space()='%s']")
    end_date_datetable = (By.XPATH, "//div[.//text()='新增服務項目']//following::tbody[4]//span[normalize-space()='%s']")
    input_service_columns = (By.XPATH, "//div[label[normalize-space()='%s']]//input")
    # aria-readonly
