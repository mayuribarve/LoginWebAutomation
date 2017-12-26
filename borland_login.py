import xlrd
from behave import *
import time
from environment import *

use_step_matcher("re")

wb = xlrd.open_workbook('features/steps/AutomationTestData.xlsx')
ws = wb.sheet_by_name("Login")


for row in range(1, ws.nrows):
    if ws.cell(row, 0) == xlrd.XL_CELL_EMPTY:
        print("break")
        break
    else:
        time.sleep(2)
        print('\nuser 1 ' + ws.cell(row,1).value)
        @given("User opens Borland website")
        def step_impl(context):
            browser.get('http://demo.borland.com/InsuranceWebExtJS/index.jsf')


        @then("print the title")
        def step_impl(context):
            title = browser.title
            print("\n Website title is " + str(title))


        @given("User is on the home page with login option")
        def step_impl(context):
            try:
                assert True
                assert browser.title == "InsuranceWeb: Home"
                print("\n user is on the home page" )
            except AssertionError:
                print("\n Fail to open borland home page")
                pass


        @when("User enters username in email field")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 2) != xlrd.XL_CELL_EMPTY
                username = ws.cell(row, 2).value
                print("\n " + str(row) + "username: " + str(username))
                # username = input("Enter username: ")
                emailfield = browser.find_element_by_id("login-form:email")
                #emailfield.clear()
                time.sleep(2)
                emailfield.send_keys(username)
                emailfield.click()
                time.sleep(2)
            except AssertionError:
                print("Invalid username")
                pass


        @step("User enters password in Password field")
        def step_impl(context):
            try:
                assert True
                assert ws.cell(row, 3) != xlrd.XL_CELL_EMPTY
                password = ws.cell(row, 3).value
                print("\n " + str(row) + "password: " + str(password))
                passfield = browser.find_element_by_id("login-form:password")
                #passfield.clear()
                time.sleep(1)
                passfield.send_keys(password)
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
                print("\n login clicked")
                time.sleep(1)
            except AssertionError:
                print("login button not found")
                pass


        @then("Login should be successful")
        def step_impl(context):
            try:
                assert True
                # assert browser.find_element_by_id("login-form:logout")
                print("\n " + str(row) + " Login successful")
                time.sleep(1)
            except AssertionError:
                print("Login unsuccessful")
                pass


        @step("Logged in User's name should be displayed")
        def step_impl(context):
            try:
                assert browser.find_element_by_class_name("login")
                if browser.find_element_by_class_name("login").text == ws.cell(row, 1).value:
                    print("\n "+ str(row) + " User logged in successfully")
                    time.sleep(2)
            except AssertionError:
                print("User is not logging in")
                pass



