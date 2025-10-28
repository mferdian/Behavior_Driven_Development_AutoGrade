from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

BASE_URL_WEB = "http://localhost:3000"

@given('The lecturer navigates to the section "Ujian" menu')
def step_navigates_exam(context):
    context.driver.get(f"{BASE_URL_WEB}/teachers/exams")
    assert "exams" in context.driver.current_url


@given('The lecturer navigates to the "Ujian" menu')
def step_exam_menu(context):
    context.driver.get(f"{BASE_URL_WEB}/teachers/exams")
    assert "exams" in context.driver.current_url

@given('The existing exam "{exam_name}" is displayed in the exam list')
def step_existing_exam(context,exam_name):
    list_exam = WebDriverWait(context.driver, 10).until(
      EC.visibility_of_element_located((By.ID, "exam-name"))
    )
    print(list_exam.text)
    assert exam_name.lower() in list_exam.text.lower()

@when('The lecturer clicks the three-dot (⋮) option next to the exam')
def step_click_option(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "option-9e58d667-b09e-4189-a2c0-9ccc626347d3"))
    )
    ActionChains(context.driver).move_to_element(button).perform()
    time.sleep(1)
    button.click()
    
@when('Selects the "View" option')
def step_click_view(context):
    view_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'view-btn'))
    )
    time.sleep(0.5)
    view_btn.click()
    
@when('Selects the "Edit" option')
def step_click_edit(context):
    edit_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'edit-btn'))
    )
    time.sleep(0.5)
    edit_btn.click()

@then('The system redirects the lecturer to "{exam_url}"')
def step_verify_redirect_exam_question(context,exam_url):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains(f"{exam_url}")
    )
    assert f"{exam_url}" in context.driver.current_url    
    
@when('The lecturer clicks the "Tambahkan Ujian" button')
def step_click_add_(context):
    add_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-exam-button"))
    )
    add_btn.click()

@when('Enters the exam name "{exam_name}"')
def step_fill_exam_input(context, exam_name):
    context.exam_name = exam_name
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-exam"))
    ).send_keys(exam_name)

@when('Updates the exam name to "{exam_name}"')
def step_fill_exam_update(context, exam_name):
    context.exam_name_update = exam_name
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "edit-exam"))
    ).send_keys(exam_name)

@when('Clicks the "Simpan Perubahan" button')
def step_click_save_update(context):
    update_btn = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.ID, "btn-save-update-exam"))
    )
    time.sleep(1)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", update_btn)
    update_btn.click()

@when('Clicks the "Tambah" button')
def step_click_save(context):
    save_btn = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.ID, "save-add-exam-button"))
    )
    time.sleep(1)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
    save_btn.click()

@when('Selects the "delete" option')
def step_click_save(context):
    delete_btn = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.ID, "delete-btn"))
    )
    time.sleep(1)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", delete_btn)
    delete_btn.click()
    

@then('The system displays the message "Success create exam"')
def step_verify_success_create(context):
    toast = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toasterr"))
    )
    assert "Success create exam".lower() in toast.text.lower()
    
@then('The system displays the message "Success update exam"')
def step_verify_success_create(context):
    toast = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toasterr"))
    )
    assert "Success update exam".lower() in toast.text.lower()

@then('The system displays the message "Success delete exam"')
def step_verify_success_create(context):
    toast = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toasterr"))
    )
    assert "Success delete exam".lower() in toast.text.lower()    
    
