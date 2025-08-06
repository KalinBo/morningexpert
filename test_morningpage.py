from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from utils.custom_logger import custom_logger
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("driver_setup")
class TestMorningexpert:

    def test_password_change_should_fail(self):
        logger = custom_logger(logging.DEBUG, logging.INFO)
        logger.info("Starting test: test_password_change_should_fail")
        try:
            new_url = "https://web.morningexpert.com/#"
            self.driver.get(new_url)
            logger.info("Opened MorningExpert web app.")
            time.sleep(2)
            login_web_app = self.driver.find_element(By.XPATH, "//a[@id='loginButton' and (text())='Login']")
            login_web_app.click()
            logger.info("Clicked Login button.")
            __username = 'kalinbobchev@gmail.com'
            __password = 'gnBcvT%4ChZJ'
            self.driver.find_element(By.XPATH,
                                     '//*[@id="my-login-screen"]/div/div/div/form/ul/li[1]/div/div/div[2]/input').send_keys(
                __username)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="my-login-screen"]/div/div/div/form/ul/li[2]/div/div/div/div/div[2]/input').send_keys(
                __password)
            logger.info("Entered credentials and attempting login...")
            elements = self.driver.find_elements(By.XPATH, "//*[@id='loginButton']")
            elements[1].click()
            time.sleep(3)
            logger.info("Login successful with temporary password.")
            self.driver.find_element(By.ID, "profile-tab").click()
            self.driver.find_element(By.XPATH, '//*[@id="settings-list"]/ul/li[4]/a').click()
            logger.info("Navigated to 'Change Password' section.")
            old_pass = self.driver.find_element(By.ID, "oldPass")
            new_pass = self.driver.find_element(By.ID, "newPass")
            confirm_pass = self.driver.find_element(By.ID, "newPass2")
            new_password = '4Psdfg()*__ABV'
            old_pass.send_keys(__password)
            confirm_pass.send_keys(Keys.TAB)
            time.sleep(2)
            new_pass.send_keys(new_password)
            confirm_pass.send_keys(Keys.TAB)
            time.sleep(2)
            confirm_pass.send_keys(new_password)
            time.sleep(2)
            confirm_pass.send_keys(Keys.TAB)
            logger.info("Attempted password change using the same temporary password as old.")
            time.sleep(2)
            change_pass_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Change']"))
            )
            logger.info("Waiting for 'Change Password' button to be clickable...")
            time.sleep(4)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", change_pass_button)
            time.sleep(10)
            self.driver.execute_script("arguments[0].click();", change_pass_button)
            logger.info("Clicking the button first time")
            logger.warning("After clicking the button nothing happens")
            time.sleep(4)
            self.driver.execute_script("arguments[0].click();", change_pass_button)
            logger.info("Clicking the button 2 time")
            logger.warning("After clicking the button nothing happens")
            time.sleep(4)
            time.sleep(4)
            self.driver.execute_script("arguments[0].click();", change_pass_button)
            logger.info("Waiting 8 seconds to click 3 time")
            logger.warning("After clicking the button nothing happens")
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", change_pass_button)
            logger.info("Clicking the button 4 time")
            logger.info("'Change Password' button clicked.")
            logger.warning("After 4 attempts to click the button and change the password, finally it worked!")

            error_massage = self.driver.find_element(By.XPATH, '//*[@id="changepass-form"]/div[4]/div/div/label')
            if error_massage.is_displayed():
                logger.warning(
                    " BUG: Password used for login does not work for changing password — inconsistent behavior.")
            else:
                logger.error(" ERROR: No error message shown, password change unexpectedly passed!")
                logger.error(
                    " BUG: Password validation is inconsistent — login accepts temporary password but change does not.")
                assert False, " ERROR: No error message shown, password change unexpectedly passed!"

        except AssertionError as ae:
            logger.error(f" Test failed: {ae}")
            raise

        except Exception as e:
            logger.exception(" Unexpected exception occurred during password change test.")
            raise