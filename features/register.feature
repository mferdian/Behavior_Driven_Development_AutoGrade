@order4
Feature: Register
  As a student
  I want to create an account
  So that I can access the website

  Scenario: Successful registration
    Given the user opens the registration page
    When the user fill in name "Student Autograde"
    And the user fill in email "studentaes@gmail.com"
    And the user fill in password "StudentAes123"
    And the user fill in confirm password "StudentAes123"
    And clicks the register "Daftar Akun" button
    Then the system should display the register message "success register user"
    And redirect to the login page

  Scenario: Failed registration due to password not match
    Given the user opens the registration page
    When the user fill in name "Student Autograde"
    And the user fill in email "studentaes1@gmail.com"
    And the user fill in password "Student_Aes123"
    And the user fill in confirm password "Student_Aes12"
    Then the system should display alert message "Passwords do not match"

  Scenario: Failed registration due to email already exists
    Given the user opens the registration page
    When the user fill in name "Student Autograde"
    And the user fill in email "student@gmail.com"
    And the user fill in password "student123"
    And the user fill in confirm password "student123"
    And clicks the register "Daftar Akun" button
    Then the system should display the register message "email already exists"