from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from code import application
from nose.tools import assert_equals
from sauceclient import SauceClient
import os


@before.all
def before_all():
    # world.app = application.app.test_client()
    # world.driver = webdriver.Chrome()

    # This is the only code you need to edit in your existing scripts.
    # The command_executor tells the test to run on Sauce, while the desired_capabilities
    # parameter tells us which browsers and OS to spin up.
    desired_cap = {
        'platform': "Linux",
        'browserName': "chrome",
        'version': "48",
        'build': os.environ['TRAVIS_BUILD_NUMBER']
    }
    username = os.environ['SAUCE_USERNAME']
    key = os.environ['SAUCE_ACCESS_KEY']
    sauce = SauceClient(username, key)
    hub_url = "%s:%s@localhost:4445" % (username, key)
    world.driver = webdriver.Remote(
        command_executor='http://%s/wd/hub' % (hub_url),
        desired_capabilities=desired_cap)

@after.all
def end(aux):
    world.driver.close()
    world.driver.quit()

@step('I have the string "(.*)"')
def i_have_the_string(step, string):
    print 'hola'

@step('I have access to web http://127.0.0.1:5000/')
def connect_to_web_page(step):
    world.driver.get("http://127.0.0.1:5000/")

@step('I introduce string "(.*)" in the text box and press ENTER')
def introduce_string_in_box(step, string):
    world.driver.implicitly_wait(10)
    login = world.driver.find_element_by_id('text-box')
    login.send_keys(string)
    login.send_keys(Keys.ENTER)

@step('I see there are results')
def check_results_are_correct(step):
    results = world.driver.find_elements_by_tag_name('td')
    if len(results) > 0:
        result_exists = True
    else:
        result_exists = False
    assert_equals(result_exists, True)

@step('I see there are no results')
def check_there_are_no_results(step):
    results = world.driver.find_elements_by_tag_name('td')
    if len(results) == 0:
        no_result_exists = True
    else:
        no_result_exists = False
    assert_equals(no_result_exists, True)

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

@step('I see an error code')
def check_an_error_code_is_shown(step):
    error = world.driver.find_element_by_id('error')
    if error:
        error_exists = True
    else:
        error_exists = False
    assert(error_exists)
