from selenium.webdriver.common.by import By


class BaseLocator:

    btn_search = (By.XPATH, "(//button[contains(@data-field-id,'_doSearch')])[last()]")
    btn_clear = (By.XPATH, "//button[contains(@data-field-id,'_doClear')]")
    btn_condition = (By.XPATH, "//button[contains(@data-field-id,'_toggle')]")

    # 下拉+篩選 選單
    select_dropdown = (By.XPATH, "//div/label[@title='%s']/following-sibling::div")
    select_option = (
        By.XPATH,
        "(//div[@class='el-scrollbar']//span[text()='%s']/parent::li)[last()]",
    )
    select_option_dropdownbase = (
        By.XPATH,
        "//div[contains(@class, 'dropdownbase')]//div[text()='%s']",
    )
    select_option_dropdownbase_first_item = (
        By.XPATH,
        "//div[contains(@class, 'dropdownbase')]//div[1]",
    )

    # span下拉選單
    select_dropdown_by_span = (
        By.XPATH,
        "//label[normalize-space()='%s']/following-sibling::span/span",
    )
    select_option_by_combobox_item = (
        By.XPATH,
        "//div[contains(@class, 'combobox-item') and text()='%s']",
    )

    btn_toolbar_item = (
        By.XPATH,
        "//div[@class='toolbar-list']//button[normalize-space()='%s']",
    )  # 轉至住客帳 #結帳
    btn_toolbar_item_2 = (By.XPATH, "(//div/button[normalize-space()='%s'])[last()]")
    btn_toolbar_item_by_panel = (
        By.XPATH,
        "//div[@class='panel-title' and text()='%s']/parent::div\
                                 /following-sibling::div//div[@class='toolbar-list']//button[normalize-space()='%s']",
    )
    btn_toolbar_with_icon = (By.XPATH, "//button[child::img[@alt='%s']]")
    btn_toolbar_with_icon_by_panel = (
        By.XPATH,
        "//div[@class='panel-title' and contains(text(), '%s')]\
                                      /parent::div/following-sibling::div//button[child::img[@alt='%s']]",
    )
    btn_close = (By.XPATH, "(//button[@title='關閉'])[last()]")
    btn_save_setting = (By.XPATH, "//button[@title='儲存' and not(contains(@class, 'e-hide'))]")
    btn_edit_setting = (By.XPATH, "//button[@title='編輯' and not(contains(@class, 'e-hide'))]")
    button_by_text = (By.XPATH, "//button[normalize-space()='%s']")

    # 字串取得或點擊
    text_by_td_field = (By.XPATH, "//td[@field='%s']")
    text_by_dropdown_input_value = (
        By.XPATH,
        "//div[@data-field-id='%s']//span[@class='e-input-value']/span",
    )
    text_ikey = (By.XPATH, "//td[@field='ikey']//div[text()='%s']")
    text_ikey_2 = (By.XPATH, "//td[@field='ikey' and text()='%s']")
    text_ikey_3 = (By.XPATH, "//td[@field='cust_mn_show_cod']/div[text()='%s']")
    text_rate_cod = (By.XPATH, "//td[@field='rate_cod']//div[text()='%s']")
    text_by_field_then_text = (By.XPATH, "//td[@field='%s']//div[text()='%s']")

    # 輸入字串
    input_by_id = (By.XPATH, "//input[@id='%s']")
    input_by_label = (By.XPATH, "(//div[child::label[normalize-space()='%s']]//input)[last()]")
    input_by_data_field_id = (By.XPATH, "//div[@data-field-id='%s']//input")
    input_condition = (By.XPATH, "//div/label[@title='%s']/following-sibling::div/input")
    input_dropdown_filter = (By.XPATH, "//span[@class='e-filter-parent']//input")

    # 通用欄位點擊 取得字串 輸入字串 點擊勾選框
    col_by_data_field_id = (By.XPATH, "//div[@data-field-id='%s']")
    text_by_field = (By.XPATH, "//td[@field='%s']/div[not (./span)]")

    text_table_items_count = (By.XPATH, "//div[@class='pagination-info']")

    # 日曆操作
    btn_date_icon = (By.XPATH, "//div[@data-field-id='%s']//span[@aria-label='select']")
    date_year_title = (By.XPATH, "//div[@class='e-day e-title']")
    date_cell_item = (
        By.XPATH,
        "//tr[not(@class)]//td[contains(@class,'e-cell')]/span[text()='%s']",
    )
