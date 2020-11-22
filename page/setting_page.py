from selenium.webdriver.common.by import By

from base.base_action import BaseAction
class SettingPage(BaseAction):
    setting_page_display = By.XPATH,"//*[@text='显示']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_display(self):
        self.click_element(self.setting_page_display)

