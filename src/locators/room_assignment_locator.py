from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class RoomAssignmentLocator(BaseLocator):

    assign_remark_icon = (By.XPATH, "//td[@field='has_assign_rmk']//i")
    select_room_no = (By.XPATH, "//div[@style='outline: none;']//div[@class='card-row']/span[text()='%s']")
    text_in_detail_tab = (By.XPATH, "//tr[contains(@id, 'OrderDtList')]//td[@field='%s']//span//input[@type='text']")
    check_room_sta = (By.XPATH, "//tr[contains(@id, 'OrderDtList')]//td[@field='assign_sta_check']//input[@type='checkbox']")
