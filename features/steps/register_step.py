from behave import given, when, then
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
import time

BASE_URL_WEB = "http://localhost:3000"

base = BaseTest()
base.setUp()

@given('the user opens the registration page')
def step_open_registration_page(context):
    base.driver.get(f"{BASE_URL_WEB}/register")

@when('the user fill in name "{name}"')
def step_fill_name(context, name):
    base.find(By.ID, "name").clear()
    base.find(By.ID, "name").send_keys(name)

@when('the user fill in email "{email}"')
def step_fill_email(context, email):
    base.find(By.ID, "email").clear()
    base.find(By.ID, "email").send_keys(email)
  
@when('the user fill in password "{password}"')
def step_fill_password(context, password):
    base.find(By.ID, "password").clear()
    base.find(By.ID, "password").send_keys(password)

@when('the user fill in confirm password "{confirm_password}"')
def step_fill_confirm_password(context, confirm_password):
    base.find(By.ID, "confirm-password").clear()
    base.find(By.ID, "confirm-password").send_keys(confirm_password)

@when('clicks the register "Daftar Akun" button')
def step_click_register_button(context):
    base.find(By.ID, "register-button").click()
    time.sleep(1)

@then('the system should display the register message "{message}"')
def step_verify_message(context, message):
    time.sleep(1)
    toast = base.driver.find_element(By.CLASS_NAME, "toasterr").text.lower()
    assert message.lower() in toast, f"Expected '{message}', but got '{toast}'"

@then('the system should display alert message "{alert_message}"')
def step_verify_alert_message(context, alert_message):
    time.sleep(1)
    alert = base.driver.find_element(By.CSS_SELECTOR, "[data-testid='confirm-password-error']").text.lower()
    assert alert_message.lower() in alert, f"Expected '{alert_message}', but got '{alert}'"

@then('redirect to the login page')
def step_redirect_login_page(context):
    time.sleep(1)
    assert "login" in base.driver.current_url

def after_all(context):
    base.tearDown()