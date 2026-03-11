from pages.base_page import BasePage


class CheckinPage(BasePage):

    def click_dialog_checkin(self):
        self.click(self.locator.btn_dialog_checkin)
        return self
