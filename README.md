# MorningExpert Automated Tests & Bug Report

Automated end-to-end tests using **Selenium**, **Pytest**, and **pytest-xdist**, supporting **parallel cross-browser testing** (Chrome, Firefox, Edge).

---

## 🐞 Bug Report: Inconsistent Password Validation

### Summary

The system **accepts a temporary password at login**, but **rejects the same password** when attempting to change it. This leads to inconsistent password validation logic between the login flow and the "Change Password" form.

### 🔁 Steps to Reproduce

1. Open [https://web.morningexpert.com/#](https://web.morningexpert.com/#)  
2. Click **Login**
3. Use:
   - **Username:** `kalinbobchev@gmail.com`  
   - **Password:** `gnBcvT%4ChZJ` (temporary password)
4. Click **Login**
5. Go to **Profile** → **Change Password**
6. Submit:
   - **Old password:** `gnBcvT%4ChZJ`
   - **New password:** `4Psdfg()*__ABV`
   - **Confirm password:** `4Psdfg()*__ABV`
7. Click **Change**

### Expected Behavior

The password should be changed successfully since the old password is valid and accepted during login.

### Actual Behavior

The form displays:
> **"Current password does not match."**

### Log Output (Selenium + Pytest)

```log
INFO - Opened MorningExpert web app.
INFO - Clicked Login button.
INFO - Entered credentials and attempting login...
INFO - Login successful with temporary password.
INFO - Navigated to 'Change Password' section.
INFO - Attempted password change using the same temporary password as old.
INFO - 'Change Password' button clicked.
WARNING - ❗ BUG: Password used for login does not work for changing password — inconsistent behavior.

**Automated Test Stack**
Tool	Purpose
Selenium WebDriver	Browser automation
Pytest	Test framework
Pytest-xdist	Parallel test execution
Chrome, Firefox, Edge	Cross-browser compatibility testing

**Installation & Setup**
Prerequisites

Python 3.8+ installed
Google Chrome, Mozilla Firefox, and Microsoft Edge installed
selenium>=4.11.0
pytest>=7.4.0
pytest-xdist>=3.3.1
Clone the Repository
Command prompt or bash
git clone https://github.com/KalinBo/morningexpert.git
cd morningexpert
pip install selenium pytest pytest-xdist


**Running Tests**
Default (Single Browser - Chrome)

pytest test_morningpage.py -v -s

Cross-Browser Parallel Testing
**Run tests in parallel across multiple browsers:**

pytest -n 3 --browser firefox --browser edge -v -s
You can specify just one and remember you have Default - Chrome:

pytest --browser firefox -v

Test Files
File	Description
test_morningexpert.py	Test for login and password change bug
conftest.py
custom_logger.py

👨‍💻 Author
Kalin Bobchev
📧 kalinbobchev@gmail.com
🔗 GitHub: github.com/KalinBo
