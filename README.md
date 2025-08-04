# MorningExpert Automated Tests & Bug Report

Automated end-to-end test suite using **Selenium**, **Pytest**, and **pytest-xdist**, with support for **parallel cross-browser execution** (Chrome, Firefox, Edge).

---

## Bug Report: Inconsistent Password Validation

### Summary

The system accepts a temporary password at login, but rejects the same password when attempting to change it. This indicates inconsistent password validation logic between the login and password change mechanisms.

### Steps to Reproduce

1. Navigate to: https://web.morningexpert.com/#  
2. Click **Login**
3. Use the following credentials:  
   - **Username:** `kalinbobchev@gmail.com`  
   - **Password:** `gnBcvT%4ChZJ` (temporary password)
4. Click **Login**
5. Navigate to **Profile** → **Change Password**
6. Fill in the form:
   - Old password: `gnBcvT%4ChZJ`
   - New password: `4Psdfg()*__ABV`
   - Confirm password: `4Psdfg()*__ABV`
7. Click **Change**

### Expected Behavior

Password should be successfully updated, as the old password is valid and was accepted at login.

### Actual Behavior

The application displays an error:

> "Current password does not match."

### Test Log Output (Pytest + Selenium)

---

## Test Stack

| Tool               | Purpose                              |
|--------------------|--------------------------------------|
| Selenium WebDriver | Browser automation                   |
| Pytest             | Python test framework                |
| pytest-xdist       | Parallel test execution              |
| Chrome / Firefox / Edge | Cross-browser compatibility testing |

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- Google Chrome, Mozilla Firefox, and Microsoft Edge
- WebDrivers (ChromeDriver, GeckoDriver, EdgeDriver) — auto-managed via Selenium Manager

### Clone the Repository

* git clone https://github.com/KalinBo/morningexpert.git
* cd morningexpert
* pip install selenium pytest pytest-xdist

### Running Tests
* If no --browser option is provided, Chrome is used as the default browser.

* To run all 3 browsers in parallel:

* pytest test_morningpage.py -n 3 --browser firefox --browser edge -v -s

### Project Structure
- test_morningpage.py - 	Main test file validating login and password change logic
- conftest.py - 	Pytest fixtures, browser setup, and CLI integration
- custom_logger.py - 	Custom logging utility for detailed test output logs
