@order2
Feature: Manage Exam Questions Functionality
  As a lecturer
  I want to manage exam questions
  So that I can add, edit, or delete questions for my exams

  Scenario: Lecturer successfully adds a new question
    Given The lecturer has selected an existing exam with id "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"
    When The lecturer clicks the "Tambahkan Soal" button
    Then The system redirects the lecturer to the new question page for exam "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"
    When The lecturer fills in the question, answer key, and maximum score fields
    And Clicks the "Simpan" button
    Then The system displays the message "success create question"
    And The system redirects the lecturer to the exam page "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"

  Scenario: Lecturer fails to add a question due to invalid input
    Given The lecturer has selected an existing exam with id "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"
    When The lecturer clicks the "Tambahkan Soal" button
    Then The system redirects the lecturer to the new question page for exam "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"
    When The lecturer fills invalid values in question form
    Then If the question text is less than 10 characters, the system displays "Question must be at least 10 characters long"
    And If the answer key is less than 10 characters, the system displays "Answer key must be at least 10 characters long"
    And If the maximum score field is filled with non-numeric input, the field will not accept the input
    And If one or more mandatory fields are not filled, the "Simpan" button is disabled

  Scenario: Lecturer edits an existing question
    Given The lecturer has selected an existing exam with id "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"
    And The lecturer has an existing question with id "a242da7d-daf1-417c-8945-f1e41aa2c7fe"
    When The lecturer clicks the options menu (three dots) and selects "Edit"
    Then The system redirects the lecturer to the edit question page for exam "851e51bc-ed0a-4abd-868a-6f4a1d413aa0" and question "a242da7d-daf1-417c-8945-f1e41aa2c7fe"
    When The lecturer modifies the question details and clicks the "Simpan" button
    Then The system displays the message "success update question"
    And The system redirects the lecturer to the exam page "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"

  Scenario: Lecturer deletes an existing question
    Given The lecturer has selected an existing exam with id "851e51bc-ed0a-4abd-868a-6f4a1d413aa0"
    And The lecturer has an existing question with id "a242da7d-daf1-417c-8945-f1e41aa2c7fe"
    When The lecturer clicks the options menu (three dots) and selects "Delete"
    Then The system displays the message "success delete question"
    And Removes the question from the list
