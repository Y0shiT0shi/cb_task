class CbrMainPage:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.implicitly_wait(15)

    def enter_reception(self):
        reception_link = self.driver.find_element_by_partial_link_text('приемная')
        reception_link.click()

    def switch_language_to_en(self):
        self.driver.find_element_by_link_text('EN').click()
