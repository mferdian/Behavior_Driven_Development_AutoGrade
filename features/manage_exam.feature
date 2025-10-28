@order2
Feature: Manage Exam Functionality
  As a lecturer
  I want to manage exam 
  So that I can add, edit, or delete exam

  Scenario: Lecturer successfully adds a new exam
    Given The lecturer navigates to the section "Ujian" menu
    When The lecturer clicks the "Tambahkan Ujian" button
    And Enters the exam name "Software Engineering"
    And Clicks the "Tambah" button
    Then The system displays the message "Success create exam"

  Scenario: Lecturer views an existing exam
    Given The lecturer navigates to the "Ujian" menu
    And The existing exam "Software Engineering" is displayed in the exam list
    When The lecturer clicks the three-dot (⋮) option next to the exam
    And Selects the "View" option
    Then The system redirects the lecturer to "/teachers/exams/9e58d667-b09e-4189-a2c0-9ccc626347d3"

  Scenario: Lecturer edits an existing exam
    Given The lecturer navigates to the "Ujian" menu
    And The existing exam "Software Engineering" is displayed in the exam list
    When The lecturer clicks the three-dot (⋮) option next to the exam
    And Selects the "Edit" option
    And Updates the exam name to "Machine Learning"
    And Clicks the "Simpan Perubahan" button
    Then The system displays the message "Success update exam"

  Scenario: Lecturer edits an existing exam
    Given The lecturer navigates to the "Ujian" menu
    And The existing exam "Software Engineering" is displayed in the exam list
    When The lecturer clicks the three-dot (⋮) option next to the exam
    And Selects the "delete" option
    Then The system displays the message "Success delete exam"

