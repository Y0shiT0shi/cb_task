class CbrGratitudePage:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.implicitly_wait(15)

    def put_gratitude_text(self, text):
        self.driver.find_element_by_id('MessageBody').send_keys(text)

    def set_agreement_flag(self):
        self.driver.find_element_by_id('_agreementFlag').click()
