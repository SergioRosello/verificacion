from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from code import application
from nose.tools import assert_equals
import time


@before.all
def before_all():
    world.app = application.app.test_client()
    world.driver = webdriver.Chrome()

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


@step('I see the results to "(.*)"')
def check_results_are_correct(step, phrase):
    time.sleep(5)
    expected_output = [u'hola', u'3', u'buenos', u'2', u'dias', u'1']
    results = world.driver.find_elements_by_tag_name('td')
    output = []
    for result in results:
        output.append(result.text)
    assert_equals(expected_output, output)

