from pages.base_page import BasePage


class TipComponent(BasePage):

    def click_ok(self):
        self.click(self.locator.btn_alert_ok)
        return self

    def click_btn_by_text(self, text):
        locator = self.formator_locator(self.locator.btn_by_text, text)
        self.click(locator)
        return self

    def get_tip_text(self):
        return self.driver.find_element(*self.locator.text_tip).text
