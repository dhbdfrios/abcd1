from selenium.webdriver.common.by import By

from base.base_action import BaseAction
class DisplayPage(BaseAction):
    display_page_search = By.XPATH,"//*[@content-desc='搜索']"
    display_page_search_content = By.CLASS_NAME,"android.widget.EditText"
    display_page_back = By.CLASS_NAME,"android.widget.ImageButton"

    def __init__(self, driver):
        super().__init__(driver)

    def click_display_search(self):
        self.click_element(self.display_page_search)

    def input_edit_content(self,content):
        self.input_element_content(self.display_page_search_content,content)

    def click_back_btn(self):
        self.click_element(self.display_page_back)
        