## 🐞 Bug: Temporary Password Accepted at Login but Rejected When Changing Password

### Summary

When a user logs in with a temporary password, authentication succeeds. However, trying to change the password using the same temporary password as the current one results in an error:  
**"Incorrect old password."**

This indicates a mismatch in password validation logic between the login and the change-password form.

---

### Steps to Reproduce

1. Go to: https://web.morningexpert.com/#  
2. Click **Login**
3. Enter credentials:
   - **Username**: `kalinbobchev@gmail.com`
   - **Password**: `gnBcvT%4ChZJ` (temporary password)
4. Click **Login**
5. Navigate to **Profile** → **Change Password**
6. Fill the form:
   - Old password: `gnBcvT%4ChZJ`
   - New password: `4Psdfg()*__ABV`
   - Confirm new password: `4Psdfg()*__ABV`
7. Click **Change**

---

### Expected Behavior

The password should be updated successfully since the old password is valid (used for login moments earlier).

---

### Actual Behavior

An error message is displayed:
> **Current password does not match.**

This prevents the password from being changed, despite being valid during login.

---

### Log Output (via Selenium + Pytest)

```log
INFO - Opened MorningExpert web app.
INFO - Clicked Login button.
INFO - Entered credentials and attempting login...
INFO - Login successful with temporary password.
INFO - Navigated to 'Change Password' section.
INFO - Attempted password change using the same temporary password as old.
INFO - 'Change Password' button clicked.
WARNING - ❗ BUG: Password used for login does not work for changing password — inconsistent behavior.

---

## How to Start This Test

### Clone the repository and install dependencies

```bash
git clone <repo-url>
start command prompt
cd <project-dir>
pip install selenium
pip install pytest

# Run the test
pytest test_morningexpert.py -s
