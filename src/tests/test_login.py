import os
import allure
from pages.login_page import LoginPage
from tools.driver_helper import DriverHelper

@allure.feature("登入頁")
class TestLogin:

    @allure.story("登入成功")
    def test_login(self):
        pages = [LoginPage]
        web = DriverHelper.create_web_browser(pages)
        web.login_page.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))
        web.login_page.screenshot('登入成功').sleep(2)
