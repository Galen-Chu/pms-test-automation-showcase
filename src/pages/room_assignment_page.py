from pages.base_page import BasePage


class RoomAssignmentPage(BasePage):

    def has_assign_rmk(self):
        assign_remark = self.driver.find_elements(*self.locator.assign_remark_icon)
        return len(assign_remark) > 0

    def select_room_no(self, room_no):
        tmp_locator = self.formator_locator(self.locator.select_room_no, room_no)
        self.click(tmp_locator)
        return self

    def get_text_in_detail_tab(self, field):
        tmp_locator = self.formator_locator(self.locator.text_in_detail_tab, field)
        return self.driver.find_element(*tmp_locator).get_attribute("value")

    def click_room_sta_checkbox(self):
        self.click(self.locator.check_room_sta)
        return self
