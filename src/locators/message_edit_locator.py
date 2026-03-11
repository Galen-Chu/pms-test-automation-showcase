from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class MessageEditLocator(BaseLocator):

    message_input_field = (By.XPATH, "//label[normalize-space()='%s']/parent::div//input[@type='text']")
    message_textarea_field = (By.XPATH, "//label[normalize-space()='留言內容']/parent::div//textarea")
    message_grid_cell = (By.XPATH, "(//div[text()='留言編輯']/ancestor::div//tr[contains(@class,'datagrid-row')]//td[%s]//div)[last()]")
    message_grid_last_row = (By.XPATH, "(//div[text()='留言編輯']/ancestor::div//tr[contains(@class,'datagrid-row')])[last()]")
