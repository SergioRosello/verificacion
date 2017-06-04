from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from code import application
from nose.tools import assert_equals
from sauceclient import SauceClient
import os

@before.all
def before_all():
    world.app = application.app.test_client()
    # world.driver = webdriver.Chrome()

    """Returns a webdriver instance of the browser specified by the
    `env_str` arg."""

    env_str = 'SELTEST_BROWSER'
    try:
        browser_nm = os.environ[env_str]
        # os.environ[key] raises a KeyError if the env. var doesn't exist
    except KeyError:
        browser_nm = 'PhantomJS'
    finally:
        world.driver = getattr(webdriver, browser_nm)()

@after.all
def end(aux):
    world.driver.close()
    world.driver.quit()

@step('I have the string "(.*)"')
def i_have_the_string(step, string):
    print 'hola'

@step('I have access to web http://127.0.0.1:8000/')
def connect_to_web_page(step):
    world.driver.implicitly_wait(10)
    world.driver.get("http://localhost:8000/")
    if not "Wordcount" in world.driver.title:
        raise Exception("Unable to load page!")

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
