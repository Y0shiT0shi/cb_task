class CbrWarningPage:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.implicitly_wait(15)

    def get_warning_content(self):
        return self.driver.find_element_by_xpath('//div[@id="content"]/p[1]').text
