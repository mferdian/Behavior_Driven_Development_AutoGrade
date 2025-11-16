from behave import given, when, then
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
import time

base = BaseTest()
base.setUp()

@given('the user opens the login page')
def step_open_login_page(context):
    base.driver.get("http://localhost:3000/login")

@when('the user enters email "{email}" and password "{password}"')
def step_enter_credentials(context, email, password):
    base.find(By.ID, "email").clear()
    base.find(By.ID, "email").send_keys(email)
    base.find(By.ID, "password").clear()
    base.find(By.ID, "password").send_keys(password)

@when('the user clicks the login button')
def step_click_login(context):
    base.find(By.ID, "login-button").click()
    time.sleep(1)

@then('the system should display the message "{message}"')
def step_verify_message(context, message):
    toast = base.driver.find_element(By.CLASS_NAME, "toasterr").text.lower()
    assert message.lower() in toast, f"Expected '{message}', but got '{toast}'"

def after_all(context):
    base.tearDown()
