from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from code import application
from nose.tools import assert_equals


@before.all
def before_all():
    world.app = application.app.test_client()
    world.driver = webdriver.Chrome()


@after.all
def end(aux):
    world.driver.close()

@step('I have the string "(.*)"')
def i_have_the_string(step, string):
    print 'hola'

@step('I have access to web http://127.0.0.1:5000/')
def connect_to_web_page(step):
    world.driver.get("http://127.0.0.1:5000/")

@step('I introduce string "(.*)" in the text box and press ENTER')
def introduce_string_in_box(step, string):
    login = world.driver.find_element_by_id('text-box')
    login.send_keys(string)
    login.send_keys(Keys.ENTER)

@step('I see the results are "(.*)"')
def check_results_are_correct(step, phrase):
    results = world.driver.find_elements_by_tag_name('td')
    output = []
    for result in results:
        output.append(result.text)
    assert_equals(phrase, unicode(output))

@step('I introduce string "(.*)" in the text box and click Reset button')
def click_reset_button_with_string_in_text_box(step, string):
    reset = world.driver.find_element_by_id('text-box')
    reset.send_keys(string)
    reset = world.driver.find_element_by_id('reset')
    reset.click()

@step('I see the text-box is empty')
def click_reset_button_with_empty_text_box(step):
    result = world.driver.find_element_by_id('text-box').text
    assert_equals(u'', result)

@step('I click the Reset button')
def click_reset_button(step):
    reset = world.driver.find_element_by_id('reset')
    reset.click()

@step('I click the Submit button')
def click_submit_button(step):
    submit = world.driver.find_element_by_id('submit')
    submit.click()