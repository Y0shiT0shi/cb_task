class CbrReceptionPage:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.implicitly_wait(15)

    def enter_gratitude(self):
        self.driver.find_element_by_link_text('Написать благодарность').click()
