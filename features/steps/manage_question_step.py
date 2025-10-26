from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL_WEB = "http://localhost:3000"

@given('The lecturer has selected an existing exam with id "{exam_id}"')
def step_select_exam(context, exam_id):
    context.exam_id = exam_id
    context.driver.get(f"{BASE_URL_WEB}/teachers/exams/{exam_id}")
    WebDriverWait(context.driver, 10).until(EC.url_contains(exam_id))
    assert exam_id in context.driver.current_url

@given('The lecturer has an existing question with id "{question_id}"')
def step_select_question(context, question_id):
    context.question_id = question_id

@when('The lecturer clicks the "Tambahkan Soal" button')
def step_click_add_question(context):
    add_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-question-button"))
    )
    add_btn.click()

@when('The lecturer clicks the options menu (three dots) and selects "Edit"')
def step_click_edit_question(context):
    menu_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, f"options-{context.question_id}"))
    )
    menu_btn.click()
    edit_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, f"edit-{context.question_id}"))
    )
    edit_btn.click()

@when('The lecturer clicks the options menu (three dots) and selects "Delete"')
def step_click_delete_question(context):
    menu_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, f"options-{context.question_id}"))
    )
    menu_btn.click()
    delete_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, f"delete-{context.question_id}"))
    )
    delete_btn.click()

@when('The lecturer fills in the question, answer key, and maximum score fields')
def step_fill_question_form(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "question"))
    ).send_keys("Apa ibu kota Indonesia?")
    context.driver.find_element(By.ID, "answer_key").send_keys("Ibu Kota Jakarta")
    context.driver.find_element(By.ID, "max_score").send_keys()

@when('Clicks the "Simpan" button')
def step_click_save(context):
    save_btn = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.ID, "save-button"))
    )
    time.sleep(1)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
    save_btn.click()

@when('The lecturer modifies the question details and clicks the "Simpan" button')
def step_modify_question(context):
    question_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "question"))
    )
    question_field.clear()
    question_field.send_keys("Apa ibu kota Republik Indonesia?")
    step_click_save(context)

@when('The lecturer fills invalid values in question form')
def step_fill_invalid_question(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "question"))
    ).send_keys("short")
    context.driver.find_element(By.ID, "answer_key").send_keys("wrong")
    score_field = context.driver.find_element(By.ID, "max_score")
    score_field.clear()
    score_field.send_keys("abc")

@then('The system redirects the lecturer to the new question page for exam "{exam_id}"')
def step_verify_redirect_new(context, exam_id):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains(f"/teachers/exams/{exam_id}/new")
    )
    assert f"/teachers/exams/{exam_id}/new" in context.driver.current_url

@then('The system redirects the lecturer to the edit question page for exam "{exam_id}" and question "{question_id}"')
def step_verify_redirect_edit(context, exam_id, question_id):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains(f"/teachers/exams/{exam_id}/edit/{question_id}")
    )
    assert f"/teachers/exams/{exam_id}/edit/{question_id}" in context.driver.current_url

@then('The system displays the message "success create question"')
def step_verify_success_create(context):
    toast = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toasterr"))
    )
    assert "success create question" in toast.text.lower()

@then('The system displays the message "success update question"')
def step_verify_success_update(context):
    toast = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toasterr"))
    )
    assert "success update question" in toast.text.lower()

@then('The system displays the message "success delete question"')
def step_verify_delete(context):
    toast = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toasterr"))
    )
    assert "success delete question" in toast.text

@then('Removes the question from the list')
def step_remove_question(context):
    items = context.driver.find_elements(By.CLASS_NAME, "question-item")
    ids = [i.get_attribute("data-id") for i in items]
    assert context.question_id not in ids

@then('The system redirects the lecturer to the exam page "{exam_id}"')
def step_redirect_to_exam(context, exam_id):
    WebDriverWait(context.driver, 10).until(
        EC.url_to_be(f"http://localhost:3000/teachers/exams/{exam_id}")
    )
    assert context.driver.current_url.endswith(f"/teachers/exams/{exam_id}")

# ------------------------
# Validation Steps
# ------------------------
@then('If the question text is less than 10 characters, the system displays "Question must be at least 10 characters long"')
def step_min_question_validation(context):
    q_field = context.driver.find_element(By.ID, "question")
    q_field.clear()
    q_field.send_keys("Pendek") 

    time.sleep(0.7)

    save_btn = context.driver.find_element(By.ID, "save-button")
    assert not save_btn.is_enabled()

    error = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='text-question']"))
    )
    assert "Question must be at least 10 characters long" in error.text.strip(), \
        f"Expected 'Question must be at least 10 characters long', got: '{error.text}'"

@then('If the answer key is less than 10 characters, the system displays "Answer key must be at least 10 characters long"')
def step_min_answer_validation(context):
    a_field = context.driver.find_element(By.ID, "answer_key")
    a_field.clear()
    a_field.send_keys("Salah")

    time.sleep(0.7)

    save_btn = context.driver.find_element(By.ID, "save-button")
    assert not save_btn.is_enabled(), "Save button should be disabled for short answer key"

    error = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='text-answer-key']"))
    )
    assert "Answer key must be at least 10 characters long" in error.text.strip(), \
        f"Expected 'Answer key must be at least 10 characters long', got: '{error.text}'"
    
@then('If the maximum score field is filled with non-numeric input, the field will not accept the input')
def step_score_numeric_validation(context):
    score_field = context.driver.find_element(By.ID, "max_score")
    score_field.clear()
    score_field.send_keys("abc")

    time.sleep(0.5)

    value = score_field.get_attribute("value")
    assert value == "" or value.isnumeric(), f"Expected numeric-only input, got: '{value}'"

@then('If one or more mandatory fields are not filled, the "Simpan" button is disabled')
def step_button_disabled(context):
    q_field = context.driver.find_element(By.ID, "question")
    a_field = context.driver.find_element(By.ID, "answer_key")
    score_field = context.driver.find_element(By.ID, "max_score")

    q_field.clear()
    a_field.clear()
    score_field.clear()

    time.sleep(0.7)

    save_btn = context.driver.find_element(By.ID, "save-button")
    assert not save_btn.is_enabled()