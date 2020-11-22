from page.setting_page import SettingPage
from page.display_page import DisplayPage
class NavigationPage:

    def __init__(self,driver):
        self.driver = driver
    @property
    def get_display_page(self):
        return DisplayPage(self.driver)

    @property
    def get_setting_page(self):
        return SettingPage(self.driver)