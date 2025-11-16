@order5
Feature: Student Exam Participation
  As a student
  I want to take an exam
  So that I can answer questions and submit my exam

  Scenario: Student enters an invalid exam token
    Given the student is on the code exam page "students/exams/do"
    When the student enters the exam token "123456"
    And clicks the "Mulai Ujian" button
    Then the system displays the message "failed token exam not found"
    And the student remains on the same page

  Scenario: Student enters a valid exam token
    Given the student is on the code exam page "students/exams/do"
    When the student enters the exam token "701456"
    And clicks the "Mulai Ujian" button
    Then the system redirects the student to "students/exams/do/274f470b-9e94-4a17-bbdf-16b6ebdaccef/1"

  Scenario: Student answers the first question
    Given the student is on the exam page "students/exams/do/274f470b-9e94-4a17-bbdf-16b6ebdaccef/1"
    When the student fills in the answer field with "Ibu meminta membeli garam di warung"
    And the student clicks the "Selanjutnya" button
    Then the system saves the student answer
    And the system redirects the student to "students/exams/do/274f470b-9e94-4a17-bbdf-16b6ebdaccef/2"

  Scenario: Student attempts to go back to the previous question manually
    Given the student is on the exam page "students/exams/do/274f470b-9e94-4a17-bbdf-16b6ebdaccef/2"
    When the student tries to manually change the URL to "students/exams/do/274f470b-9e94-4a17-bbdf-16b6ebdaccef/1"
    Then the system prevents navigation
    And keeps the student on the current page

  Scenario: Student submits the final answer
    Given the student is on the exam page "students/exams/do/274f470b-9e94-4a17-bbdf-16b6ebdaccef/2"
    When the student clicks the "Selesaikan Ujian" button
    Then the system displays the message "success submit essay"
    And redirects the student to the exam page "students/exams/do"
