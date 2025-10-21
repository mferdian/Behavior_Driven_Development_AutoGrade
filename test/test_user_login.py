from utils.base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class LecturerLoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_url = "http://localhost:3000/login"  

    def test_lecturer_login_success(self):
        """Scenario: Successful login as Lecturer"""
        self.driver.get(self.login_url)
        self.find(By.ID, "email").send_keys("michael01@gmail.com")
        self.find(By.ID, "password").send_keys("password123")
        self.find(By.ID, "login-button").click()
        
        time.sleep(1)
        
        success_message = self.driver.find_element(By.CLASS_NAME, "toasterr").text
        self.assertIn("success login user", success_message.lower())

    def test_lecturer_login_failed_invalid_credentials(self):
        """Scenario: Failed login due to invalid credentials (Lecturer)"""
        self.driver.get(self.login_url)
        self.find(By.ID, "email").send_keys("michael01@gmail.com")
        self.find(By.ID, "password").send_keys("password12")
        self.find(By.ID, "login-button").click()

        time.sleep(1)
        
        error_message = self.driver.find_element(By.CLASS_NAME, "toasterr").text
        self.assertIn("invalid login credentials", error_message.lower())


class StudentLoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_url = "http://localhost:3000/login"  # ganti sesuai URL login sistem kamu

    def test_student_login_success(self):
        """Scenario: Successful login as Student"""
        self.driver.get(self.login_url)
        self.find(By.ID, "email").send_keys("andi88@gmail.com")
        self.find(By.ID, "password").send_keys("userpass123")
        self.find(By.ID, "login-button").click()
        
        time.sleep(1)
        
        # Tunggu hingga dashboard lecturer muncul
        success_message = self.driver.find_element(By.CLASS_NAME, "toasterr").text
        self.assertIn("success login user", success_message.lower())

    def test_student_login_failed_invalid_credentials(self):
        """Scenario: Failed login due to invalid credentials (Student)"""
        self.driver.get(self.login_url)
        self.find(By.ID, "email").send_keys("andi88@gmail.com")
        self.find(By.ID, "password").send_keys("password123")
        self.find(By.ID, "login-button").click()

        time.sleep(1)
        
        error_message = self.driver.find_element(By.CLASS_NAME, "toasterr").text
        self.assertIn("invalid login credentials", error_message.lower())
