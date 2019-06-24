from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyscreenshot
import pyautogui


@given('start google search')
def step_impl(context):
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    # driver.maximize_window()
    driver.get('https://www.google.ru')
    assert 'Google' in driver.title
    search_form = driver.find_element_by_name('q')
    search_form.send_keys('Центральный банк РФ')
    search_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="btnK"]')))
    search_btn.click()
    cbr_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"cbr.ru")]')))
    cbr_link.click()
    #tabs = driver.window_handles
    #for tab in tabs:
    #    driver.switch_to.window(tab)
    #    if driver.current_url == 'https://www.cbr.ru':
    #        driver.find_element_by_partial_link_text('приемная').click()


    time.sleep(3)
    # print(driver.window_handles)
    #driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.window(driver.window_handles[1])


    #reception_link = driver.find_element_by_xpath('//a[href="/Reception/"]')
    reception_link = driver.find_element_by_partial_link_text('приемная')
    reception_link.click()
    driver.find_element_by_link_text('Написать благодарность').click()
    driver.find_element_by_id('MessageBody').send_keys('случайный текст')
    driver.find_element_by_id('_agreementFlag').click()
    pyautogui.screenshot('scr.png')
    driver.find_element_by_class_name('burger').click()
    driver.find_element_by_xpath('//a[@class="pseudo" and contains(@href,"About")]').click()
    driver.find_element_by_link_text('Предупреждение').click()
    ru_warning = driver.find_element_by_xpath('//div[@id="content"]/p[1]').text
    with open('warning.txt', 'w') as f:
        f.write(ru_warning)
    driver.find_element_by_link_text('EN').click()
    en_warning = driver.find_element_by_xpath('//div[@id="content"]/p[1]').text
    # with open('log.txt','w') as f:
    #     tabs = driver.window_handles
    #     for tab in tabs:
    #         driver.switch_to.window(tab)
    #         f.write(driver.current_url + '\n')
