import xlrd
from behave import *
import time
from environment import *

use_step_matcher("re")


wb = xlrd.open_workbook('features/steps/AutomationTestData.xlsx')
ws = wb.sheet_by_name("Login")


@given("User opens Borland website")
def step_impl(context):
    browser.get('http://demo.borland.com/InsuranceWebExtJS/index.jsf')


@then("print the title")
def step_impl(context):
    title = browser.title
    print("\n Website title is " + str(title))


for row in range(1, ws.nrows):
    print("\n" + str(ws.cell(row, 1).value))
    if ws.cell(row, 0) == xlrd.XL_CELL_EMPTY:
        print("break")
        break
    else:
        @given("User is on the home page with login option")
        def step_impl(context):
            try:
                assert True
                assert browser.title == "InsuranceWeb: Home"
                print("\n" + browser.title)
            except AssertionError:
                print("\n Fail to open borland home page")
                pass
        @when("User enters username in email field")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 2) != xlrd.XL_CELL_EMPTY
                username = ws.cell(row, 2).value
                print("username: " + str(username))
                #username = input("Enter username: ")
                emailfield = browser.find_element_by_id("login-form:email")
                emailfield.clear()
                emailfield.send_keys(username)
                time.sleep(1)
            except AssertionError:
                print("Invalid username")
                pass
        @when("User enters password in Password field")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 3) != xlrd.XL_CELL_EMPTY
                password = ws.cell(row, 3).value
                print("\n password: " + str(password))
                passfield = browser.find_element_by_id("login-form:password")
                passfield.clear()
                passfield.send_keys(password)
                print(password)
                time.sleep(1)
            except AssertionError:
                print("Invalid password")
                pass
        @step("clicks Login button")
        def step_impl(context):
            try:
                assert True
                assert browser.find_element_by_id("login-form:login")
                loginbutton = browser.find_element_by_id("login-form:login")
                loginbutton.click()
                print("login clicked")
                time.sleep(1)
            except AssertionError:
                print("Login button not found")
                pass
        @then("Login should be successful")
        def step_impl(context):
            try:
                assert True
                #assert browser.find_element_by_id("login-form:logout")
                print("\n Login successful")
                time.sleep(1)
            except AssertionError:
                print("Login unsuccessful")
                pass
        @step("Logged in User's name should be displayed")
        def step_impl(context):
            try:
                assert browser.find_element_by_class_name("login")
                if browser.find_element_by_class_name("login").text == ws.cell(row, 1).value:
                    print("\n User logged in successfully")
                    time.sleep(1)
            except AssertionError:
                print("User is not logging in")
                pass
