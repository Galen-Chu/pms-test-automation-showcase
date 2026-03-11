from pages.base_page import BasePage


class HomePage(BasePage):

    def to_pms_page(self):
        self.click(self.locator.btn_pms)
        return self
