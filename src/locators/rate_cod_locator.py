from selenium.webdriver.common.by import By


class RateCodLocator:

    btn_add_use_date = (By.XPATH, "//div[@data-field-id='doOpenUseTime']")
    btn_add_new_use_date = (
        By.XPATH,
        "//div[contains(@id, 'dialog_') and descendant::div[contains(normalize-space(), '使用期間')]]\
                            /following-sibling::div//div[@data-field-id='grid-add']",
    )
    btn_date_icon = (By.XPATH, "//div[@data-field-id='%s']//span[@aria-label='select']")
    date_year_title = (By.XPATH, "//div[@class='e-day e-title']")
    date_cell_item = (
        By.XPATH,
        "//tr[not(@class)]//td[contains(@class,'e-cell')]/span[text()='%s']",
    )
    btn_by_id = (By.XPATH, "//div[@data-field-id='%s']")
    btn_by_id_down = (
        By.XPATH,
        "//div[@data-field-id='%s']//span[@class='e-input-group-icon e-ddl-icon']",
    )
    select_item = (By.XPATH, "//li[@class='e-list-item']/span[normalize-space()='%s']")

    tab_name = (By.XPATH, "//div[@id='tab-%s']")
    td_price = (
        By.XPATH,
        "//div[@id='pane-%s']//tr[child::td[normalize-space()='%s']]//span[@class='e-cellvalue']",
    )
    input_price = (
        By.XPATH,
        "//div[@id='pane-%s']//tr[child::td[normalize-space()='%s']]//input[not(@validatehidden)]",
    )
    btn_pnael_close = (
        By.XPATH,
        "//div[@class='e-dlg-header' and descendant::div[text()='房價']]/preceding-sibling::button[@title='關閉']",
    )
    btn_localization_ratecod = (
        By.XPATH,
        "//div[@data-field-id='ratecodeName']/span[contains(@class, 'e-input-group-icon')]",
    )
    btn_edit_lang = (
        By.XPATH,
        "//tr[@role='row' and child::td[normalize-space()='%s']]//button[not(contains(@class,'e-hide'))]",
    )
    input_lang_col = (
        By.XPATH,
        "//tr//td[descendant::input[@value='%s']]/following-sibling::td//input",
    )
    btn_save_lang = (
        By.XPATH,
        "//tr//td[descendant::input[@value='%s']]/preceding-sibling::td//button[@title='儲存']",
    )
    btn_lang_confirm = (By.XPATH, "//div[@data-field-id='confirmButton']")
    btn_grid_add = (By.XPATH, "//div[@data-field-id='grid-add']")

    select_charge_type = (By.XPATH, "//div[@data-field-id='chargeType']")
    item_service_types = (By.XPATH, "//ul[@role='listbox']//li")

    icon_sell_from_date = (
        By.XPATH,
        "//div[@data-field-id='sellFromDate']//span[@aria-label='select']",
    )
    date_range_year_title = (
        By.XPATH,
        "//div[@class='e-%s-container']//div[@class='e-day e-title']",
    )
    date_range_cell_item = (
        By.XPATH,
        "//div[@class='e-%s-container']//tr[not(@class)]//td[contains(@class,'e-cell')]\
                            /span[not(@aria-disabled) and text()='%s']",
    )

    text_cratecod_mn = (By.XPATH, "//td[@field='altName' and text()='%s']")

    btn_add_service_item = (By.XPATH, "//div[@data-field-id='grid-add']")
    btn_dropdown_all = (By.XPATH, "//span[@class='e-all-text']")
    label_span_select_item = (
        By.XPATH,
        "//li[contains(@class, 'e-list-item') and normalize-space()='%s']",
    )

    grid_disabled = (By.XPATH, "//div[contains(@class, 'disablegrid')]")
    btn_toolbar_item_by_panel = (By.XPATH, "//button[text()='%s']")
