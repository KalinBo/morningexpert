# MorningExpert Automated Tests & Bug Report

## 🐞 Bug Report: Temporary Password Accepted at Login but Rejected When Changing Password

### Summary

When logging in with a temporary password, authentication succeeds. However, trying to change the password by submitting the same temporary password as the current one results in the error:

> **"Current password does not match."**

This points to inconsistent password validation logic between login and password change.

---

### Steps to Reproduce

1. Open [https://web.morningexpert.com/#](https://web.morningexpert.com/#)  
2. Click **Login**  
3. Enter credentials:  
   - **Username**: `kalinbobchev@gmail.com`  
   - **Password**: `gnBcvT%4ChZJ` (temporary password)  
4. Click **Login**  
5. Navigate to **Profile** → **Change Password**  
6. Fill in the form:  
   - Old password: `gnBcvT%4ChZJ`  
   - New password: `4Psdfg()*__ABV`  
   - Confirm new password: `4Psdfg()*__ABV`  
7. Click **Change**

---

### Expected Behavior

The password should be successfully updated because the old password used for login is correct.

---

### Actual Behavior

An error message appears:

> **Current password does not match.**

Password change is blocked despite correct credentials.

---

### Log Output (from Selenium + Pytest)

```log
INFO - Opened MorningExpert web app.
INFO - Clicked Login button.
INFO - Entered credentials and attempting login...
INFO - Login successful with temporary password.
INFO - Navigated to 'Change Password' section.
INFO - Attempted password change using the same temporary password as old.
INFO - 'Change Password' button clicked.
WARNING - ❗ BUG: Password used for login does not work for changing password — inconsistent behavior.


How to Run the Automated Test

Python 3.x installed

Installation
Clone the repository and install required Python packages:
git clone https://github.com/KalinBo/morningexpert.git
cd morningexpert
pip install selenium
pip install pytest

Execute the test file using pytest:
pytest test_morningexpert.py -s
