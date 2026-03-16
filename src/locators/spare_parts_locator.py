from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class SparePartsLocator(BaseLocator):

    btn_add_spare_parts = (By.XPATH, "//span[@class='button-add--s']")
    btn_remove_spare_parts = (By.XPATH, "//span[@class='button-remove--s']")

    # 右側表格
    spare_parts_table_by_date = (By.XPATH, "//tr[td/div[contains(text(),'%s')]]/td/div")

    # 明細
    spare_parts_first_row = (
        By.XPATH,
        "//tr[contains(@id,'gid') and (child::td[@field='modifyButton'])]",
    )
    spare_parts_row_dropdown = (By.XPATH, "//td[@field='%s']//a")
    spare_parts_options = (By.XPATH, "//div[@class='combobox-item' and text()='%s']")
    spare_parts_label = (By.XPATH, "(//td[@field='%s']//input)[last()-1]")
    spare_parts_toolbar = (By.XPATH, "//div[@class='toolbar']//button[normalize-space()='%s']")

    # 日期選擇
    calendar_title = (
        By.XPATH,
        "(//div[@class='calendar-title' and span[text()='Jan 2024']])[last()]",
    )
    input_year = (
        By.XPATH,
        "(//span[text()='Jan 2024'])[last()]/ancestor::div[contains(@class,'datebox')]//input",
    )
    select_date = (
        By.XPATH,
        "(//span[text()='Jan 2024'])[last()]/ancestor::div[contains(@class,'datebox')]//td[text()='%s']",
    )
