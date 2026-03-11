from selenium.webdriver.common.by import By


class LostItemLocator():
    # ----- 編輯失物 視窗欄位 -----

    # -- 下拉選單 --
    status_dropdown = (By.XPATH, "//label[normalize-space()='狀態']/parent::div//a")
    status_options = (By.XPATH, "//div[contains(@class, 'combo-panel')]//div[text()= '%s']")
    loser_name_dropdown = (By.XPATH, "//label[normalize-space()='遺失者']/parent::div//a")
    loser_name_options = (By.XPATH, "//div[contains(@class, 'combo-panel')]//tr[@datagrid-row-index='0']")
    # -- 下拉選單 End --
    # -- 日期選單 --
    date_by_field = (By.XPATH, "//label[normalize-space()='%s']/following-sibling::div/input")
    btn_date = (By.XPATH, "//span[contains(text(), '年') and @role='button']")
    date_year = (By.XPATH, "//table[@class='el-year-table']//a[text()='%s']")
    date_mon = (By.XPATH, "//table[@class='el-month-table']//a[text()='%s']")
    date_day = (By.XPATH, "//table[@class='el-date-table']//td[normalize-space()='%s']")
    # -- 日期選單 End --
    # -- 欄位編輯 --
    loser_name_field = (By.XPATH, "//label[normalize-space()='遺失者']/following-sibling::span/input[@type='text']")
    # -- 欄位編輯 End --

    # ----- 編輯失物 視窗欄位 End -----

    # ----- 拾獲者領回 視窗欄位 -----
    claim_note_field = (By.XPATH, "//textarea[preceding::label[normalize-space()='領回備註']]")
    # ----- 拾獲者領回 視窗欄位 End -----

    # ----- 右側表格 資料顯示 -----
    text_data_in_dialog = (By.XPATH, "//div[@class='panel window panel-htop']//tr[@datagrid-row-index='0']//td[@field='%s']")
    # ----- 右側表格 資料顯示 End -----
