@order1
Feature: User Login Functionality

  Scenario: Lecturer successfully logs in
    Given the user opens the login page
    When the user enters email "michael01@gmail.com" and password "password123"
    And the user clicks the login button
    Then the system should display the message "success login user"

  Scenario: Lecturer login fails with invalid credentials
    Given the user opens the login page
    When the user enters email "michael01@gmail.com" and password "password12"
    And the user clicks the login button
    Then the system should display the message "invalid login credentials"

  Scenario: Student successfully logs in
    Given the user opens the login page
    When the user enters email "andi88@gmail.com" and password "userpass123"
    And the user clicks the login button
    Then the system should display the message "success login user"

  Scenario: Student login fails with invalid credentials
    Given the user opens the login page
    When the user enters email "andi88@gmail.com" and password "password123"
    And the user clicks the login button
    Then the system should display the message "invalid login credentials"
