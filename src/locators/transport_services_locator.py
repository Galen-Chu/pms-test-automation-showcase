from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class TransportServicesLocator(BaseLocator):
    # 視窗元素
    btn_batch_add_transport = (By.XPATH, "//button[normalize-space()='批次新增']")
    btn_save_batch_add_transport = (By.XPATH, "(//button[child::img[@alt='save']])[last()]")
    transport_auto_charge_checkbox = (By.XPATH, "//label[contains(@class, 'el-checkbox') and contains(., '自動入帳')]")
    transport_time_confirm_btn = (By.XPATH, "//button[normalize-space()='確認']")

    # 驗證用 locators - 參數化表單欄位 (標籤文字作為參數)
    transport_field_with_div = (By.XPATH, "//label[normalize-space()='%s']/following-sibling::div//input")
    transport_field_direct = (By.XPATH, "//label[normalize-space()='%s']/following-sibling::input")
    transport_field_spinbutton = (By.XPATH, "//label[normalize-space()='%s']/following-sibling::div//input[@role='spinbutton']")
    transport_field_combobox_text = (By.XPATH, "//label[normalize-space()='%s']/parent::div//input[contains(@class, 'textbox-text')]")
    transport_type_option = (By.XPATH, "//div[text()='%s']")

    # 接送服務資料表格
    transport_grid_cell = (By.XPATH, "(//div[text()='接送服務編輯']/ancestor::div//tr[contains(@class,'datagrid-row')]//td[%s]//div)[last()]")
    transport_data_rows = (By.XPATH, "//table//tr[td[contains(.,'A : 接') or contains(.,'L : 送')]]")
    transport_grid_last_row = (By.XPATH, "(//table//tr[td[contains(.,'A : 接') or contains(.,'L : 送')]])[last()]")
    transport_data_row_by_index = (By.XPATH, "//table//tr[td[contains(.,'A : 接') or contains(.,'A : 送')]][%s]")
    transport_data_colume_by_row_and_index = (By.XPATH, "//table//tr[td[contains(.,'A : 接') or contains(.,'A : 送')]][%s]//td[%s]")
