from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions as exc


class GoogleMainPage:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.google.ru')
        assert 'Google' in self.driver.title

    def check_google_is_opened(self):
        try:
            self.driver.find_element_by_name('q')
        except exc.NoSuchElementException:
            print('Похоже, что google не открылся')

    def enter_text_for_search(self, text):
        search_form = self.driver.find_element_by_name('q')
        search_form.send_keys(text)

    def press_search_button(self):
        search_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="btnK"]')))
        search_btn.click()

    def check_link_in_results(self, link):
        try:
            link_obj = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"' + link + '")]')))
            return link_obj
        except exc.NoSuchElementException:
            print('Похоже, что нет ссылки в результатах поиска')

    def click_link_in_results(self, link):
        link.click()

    # def check_tab_with_title_exist(self, title):
    #     tabs = self.driver.window_handles
    #     with open('log.txt', 'w') as f:
    #         for tab in tabs:
    #             self.driver.switch_to.window(tab)
    #             f.write(self.driver.title + '\n')
    #             if title == self.driver.title:
    #                 return tab
    #             else:
    #                 return None

    def check_title(self, title):
        if title == self.driver.title:
            return True
        else:
            return False