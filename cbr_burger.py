class CbrBurger:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.implicitly_wait(15)

    def enter_burger(self):
        self.driver.find_element_by_class_name('burger').click()

    def enter_about(self):
        self.driver.find_element_by_xpath('//a[@class="pseudo" and contains(@href,"About")]').click()

    def enter_about_warning(self):
        self.driver.find_element_by_link_text('Предупреждение').click()
