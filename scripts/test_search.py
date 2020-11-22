import pytest

from base.base_driver import init_driver
from page.nava_page import NavigationPage
import time,yaml


def read_data_yaml():
    with open('../data/data.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        return data

class Test_Search:
    #前置代码
    def setup(self):
        #1.初始化driver
        self.driver = init_driver()
        #2.初始化page
        self.navigation_page = NavigationPage(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    @pytest.mark.parametrize("content",read_data_yaml())
    def test_search(self,content):
         self.navigation_page.get_setting_page.click_display()
         self.navigation_page.get_display_page.click_display_search()
         self.navigation_page.get_display_page.input_edit_content(content)
         self.navigation_page.get_display_page.click_back_btn()

 