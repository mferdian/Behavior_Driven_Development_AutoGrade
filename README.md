## 🧪 Behavior-Driven Development (BDD) Login Testing with Behave & Selenium

### 📘 Overview

This project demonstrates the implementation of **Behavior-Driven Development (BDD)** testing for a web-based login system using **Behave** and **Selenium WebDriver** in Python.

The goal is to test both **Lecturer** and **Student** login functionalities, ensuring that the system behaves correctly according to the defined user stories.

---

### 🧱 Project Structure

```
project/
│
├── features/
│   ├── login.feature                # BDD Scenarios written in Gherkin
│   └── steps/
│       └── login_steps.py           # Step definitions implemented in Python
│
├── utils/
│   └── base_test.py                 # Base class for WebDriver setup and helper methods
│
├── requirements.txt                 # Dependencies list
└── README.md                        # Project documentation
```

---

### ⚙️ Requirements

Make sure you have **Python 3.8+** installed.
Then, install the dependencies listed below:

```bash
pip install -r requirements.txt
```

#### 📦 Contents of `requirements.txt`

```txt
behave
selenium
webdriver-manager
pytest
```

---

### 🚀 How to Run the Tests

1. **Ensure Chrome browser is installed** on your computer.
   (ChromeDriver will be automatically managed by `webdriver-manager`.)

2. **Start your web application** (e.g., `http://localhost:3000/login`).

3. **Run all BDD test scenarios** using the following command:

   ```bash
   behave
   ```

4. **Expected output example:**

   ```bash
   Feature: User Login Functionality

     Scenario: Lecturer successfully logs in
       Given the user opens the login page
       When the user enters email "michael01@gmail.com" and password "password123"
       And clicks the "Login" button
       Then the system should display the message "success login user"
       ✅ Passed

     Scenario: Student login fails with invalid credentials
       Given the user opens the login page
       ...
       ✅ Passed

   4 scenarios passed (4 passed)
   0 failed, 0 skipped
   ```

---

### 🧩 BDD Feature Explanation

#### 📄 `features/login.feature`

Written in **Gherkin syntax**, describing test behavior in natural English:

```gherkin
Feature: User Login Functionality

  Scenario: Lecturer successfully logs in
    Given the user opens the login page
    When the user enters email "michael01@gmail.com" and password "password123"
    And clicks the "Login" button
    Then the system should display the message "success login user"
```

This format allows developers, testers, and non-technical stakeholders to **understand the system behavior clearly** without needing to read the code.

---

### 💻 Step Definitions

#### 🧠 `features/steps/login_steps.py`

This file implements the behavior described in `login.feature` using **Selenium WebDriver** and the helper class from `utils/base_test.py`.

Example:

```python
@given('the user opens the login page')
def step_open_login_page(context):
    base.driver.get("http://localhost:3000/login")
```

---

### 🔧 `utils/base_test.py`

Handles browser setup and utility methods:

* Launches and configures Chrome WebDriver.
* Provides reusable helper methods like:

  * `find(by, locator)`
  * `wait_for(by, locator)`
  * `click_and_wait(by, locator)`

Example:

```python
def setUp(self):
    service = Service(ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=service, options=chrome_options)
    self.wait = WebDriverWait(self.driver, 10)
```

---

### 🧾 Test Scenarios Included

| No | Scenario Description                  | Expected Result                             |
| -- | ------------------------------------- | ------------------------------------------- |
| 1  | Lecturer login with valid credentials | “success login user” message appears        |
| 2  | Lecturer login with invalid password  | “invalid login credentials” message appears |
| 3  | Student login with valid credentials  | “success login user” message appears        |
| 4  | Student login with invalid password   | “invalid login credentials” message appears |

---

### 📊 Key Concepts Highlighted

* **Behavior-Driven Development (BDD)** methodology.
* **Readable test cases** using Gherkin (`Given–When–Then`).
* **Automated UI testing** via Selenium WebDriver.
* **Reusability & maintainability** through BaseTest abstraction.

---

### 🧠 Why Use BDD?

BDD bridges the gap between:

* **Developers**, who write the logic,
* **Testers**, who validate behavior, and
* **Stakeholders**, who define business goals.

This ensures that the **system is built and tested based on expected user behavior**, not just technical correctness.

---

### 🧹 Clean Up

After the tests finish, Behave automatically quits the browser instance using `base.tearDown()` to prevent leftover Chrome processes.

---

### 🏁 Summary

| Tool                  | Purpose                              |
| --------------------- | ------------------------------------ |
| **Behave**            | Define human-readable test scenarios |
| **Selenium**          | Automate browser interactions        |
| **webdriver-manager** | Manage ChromeDriver automatically    |
| **BaseTest**          | Reusable setup and helper functions  |

---

Would you like me to make the **README version for the old unittest-style BDD (like the one in your PDF)** too — so you can show both approaches side by side in your report?
