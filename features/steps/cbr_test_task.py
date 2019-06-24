from behave import *
import googlesearch
import time
from selenium import webdriver
import cbr_burger
import cbr_gratitude_page
import cbr_main_page
import cbr_reception_page
import cbr_warning_page
import pyautogui
import random

driver = webdriver.Firefox()


@given('enter google site')
def step_impl(context):
    context.google_page = googlesearch.GoogleMainPage(driver)

@then('check for search field')
def step_impl(context):
    context.google_page.check_google_is_opened()

@then('enter cbr in search field')
def step_impl(context):
    context.google_page.enter_text_for_search('Центральный банк РФ')

@then('press search button')
def step_impl(context):
    context.google_page.press_search_button()

@then('find cbr.ru link')
def step_impl(context):
    context.link = context.google_page.check_link_in_results('cbr.ru')

@then('press link')
def step_impl(context):
    context.google_page.click_link_in_results(context.link)
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])

@then('check site is opened')
def step_impl(context):
    if not context.google_page.check_title('Центральный банк Российской Федерации'):
        print('Открылся другой сайт')
    else:
        context.main_page = cbr_main_page.CbrMainPage(driver)

@then('enter reception')
def step_impl(context):
    context.main_page.enter_reception()
    context.reception_page = cbr_reception_page.CbrReceptionPage(driver)

@then('enter gratitude')
def step_impl(context):
    context.reception_page.enter_gratitude()
    context.gratitude_page = cbr_gratitude_page.CbrGratitudePage(driver)

@then('write gratitude text')
def step_impl(context):
    context.gratitude_page.put_gratitude_text('Случайный текст')

@then('set agreement')
def step_impl(context):
    context.gratitude_page.set_agreement_flag()

@then('make screenshot')
def step_impl(context):
    pyautogui.screenshot('scr' + str(random.random()) + '.png')

@then('click burger')
def step_impl(context):
    context.burger_element = cbr_burger.CbrBurger(driver)
    context.burger_element.enter_burger()

@then('enter about')
def step_impl(context):
    context.burger_element.enter_about()

@then('enter warning')
def step_impl(context):
    context.burger_element.enter_about_warning()
    context.warning_page = cbr_warning_page.CbrWarningPage(driver)

@then('get text warning')
def step_impl(context):
    context.ru_warning_text = context.warning_page.get_warning_content()

@then('change language')
def step_impl(context):
    context.main_page.switch_language_to_en()

@then('check language is changed')
def step_impl(context):
    context.en_warning_text = context.warning_page.get_warning_content()
    assert context.ru_warning_text != context.en_warning_text
