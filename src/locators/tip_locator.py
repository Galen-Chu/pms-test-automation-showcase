from selenium.webdriver.common.by import By

class TipLocator:

    btn_alert_ok = (By.XPATH, "//div[@role='dialog' and @aria-label='提示']//button[@data-field-id='alertOK']")
    btn_by_text = (By.XPATH, "//div[@role='dialog' and @aria-label='提示']//button/span[normalize-space()='%s']")
    text_tip = (By.XPATH, "//div[@role='dialog' and @aria-label='提示']//p//p")
