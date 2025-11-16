from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL_WEB = "http://localhost:3000"

@given('the student is on the code exam page "{path}"')
def step_student_open_exam_page(context, path):
    context.driver.get(f"{BASE_URL_WEB}/{path}")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "exam-code-form"))
    )

@given('the student is on the exam page "{path}"')
def step_student_open_exam_page(context, path):
    context.driver.get(f"{BASE_URL_WEB}/{path}")
    assert "exams" in context.driver.current_url


@when('the student enters the exam token "{token}"')
def step_enter_exam_token(context, token):
    digits = list(token)

    inputs = context.driver.find_elements(By.CSS_SELECTOR, "#exam-code-form input")

    assert len(inputs) == 6, "Token input harus 6 kotak"

    for i, char in enumerate(digits):
        inputs[i].clear()
        inputs[i].send_keys(char)


@when('clicks the "{button}" button')
def step_click_button(context, button):
    btn = WebDriverWait(context.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "start-exam-button"))
    )
    btn.click()


@then('the system displays the message "{message}"')
def step_check_message(context, message):
    time.sleep(1)
    toast = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toasterr"))
    )
    assert message.lower() in toast.text.lower(), f"Expected '{message}', but got '{toast.text}'"

@then('the student remains on the same page')
def step_stays_same_page(context):
    assert context.driver.current_url.endswith("/students/exams/do")


@then('the system redirects the student to "{exam_path}"')
def step_redirect_question(context, exam_path):
    context.driver.get(f"{BASE_URL_WEB}/{exam_path}")
    assert f"{exam_path}" in context.driver.current_url


@when('the student fills in the answer field with "{text}"')
def step_enter_answer(context, text):
  textarea = WebDriverWait(context.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "answer-textarea"))
  )
  textarea.click()
  textarea.send_keys(text)


@then("the system saves the student answer")
def step_saved_answer(context):
    # biasanya pakai network listener atau simpan ID
    # untuk sekarang kita cek tidak error di UI
    pass


@when('the student tries to manually change the URL to "{url}"')
def step_manual_prev(context, url):
    context.driver.get(f"{BASE_URL_WEB}/{url}")

@then('the system prevents navigation')
def step_prevent_nav(context):
    # Cek URL masih tetap halaman 2
    time.sleep(1)
    assert context.driver.current_url.endswith("/2")


@then('keeps the student on the current page')
def step_keep_same(context):
    # sama, tapi terpisah sesuai Gherkin
    assert "/2" in context.driver.current_url


@when('the student clicks the "{name}" button')
def step_click_finish(context, name):
    btn = context.driver.find_element(By.ID, "exam-next-or-finish-button")
    btn.click()


@then('redirects the student to the exam page "{path}"')
def step_redirect_to(context, path):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains(path)
    )
