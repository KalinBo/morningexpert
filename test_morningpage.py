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


@pytest.mark.usefixtures("setup", "onetimesetup")
class TestMorningexpert:
    def setup_method(self):
        options = Options()
        prefs = {
            "profile.default_content_setting_values.notifications": 2
        }
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()


    # def test_youtube(self):
    #     original_window = self.driver.current_window_handle
    #     first_youtube = self.driver.find_element(By.XPATH, '//*[@id="home"]/ul/li[4]/a')
    #     self.driver.execute_script(
    #         "window.open(arguments[0].href, 'https://www.youtube.com/channel/UCdXg9VKrpTDo2V5Ys-DDdOA');",
    #         first_youtube)
    #     time.sleep(3)
    #     self.driver.switch_to.window(original_window)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    #     youtube = self.driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div[1]/ul/li[4]/a')
    #     youtube.click()
    #     time.sleep(3)
    #     bizki = self.wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')))
    #     bizki.click()
    #     time.sleep(8)


    # This is only the login
    # def test_login(self):
    #     new_url = "https://web.morningexpert.com/#"
    #     self.driver.get(new_url)
    #     time.sleep(2)
    #     time.sleep(1)
    #     login_web_app = self.driver.find_element(By.XPATH, "//a[@id='loginButton' and (text())='Login']")
    #     login_web_app.click()
    #     time.sleep(2)
    #     __username = 'kalinbobchev@gmail.com'
    #     __password = 'gnBcvT%4ChZJ'
    #     self.driver.find_element(By.XPATH,
    #                              '//*[@id="my-login-screen"]/div/div/div/form/ul/li[1]/div/div/div[2]/input').send_keys(
    #         __username)
    #     self.driver.find_element(By.XPATH,
    #                              '//*[@id="my-login-screen"]/div/div/div/form/ul/li[2]/div/div/div/div/div[2]/input').send_keys(
    #         __password)
    #     time.sleep(2)
    #     elements = self.driver.find_elements(By.XPATH, "//*[@id='loginButton']")
    #     elements[1].click()
    #     assert elements
    #     time.sleep(2)

    def tst_password_change_should_fail(self):
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
                    "❗ BUG: Password used for login does not work for changing password — inconsistent behavior.")
            else:
                logger.error("❌ ERROR: No error message shown, password change unexpectedly passed!")
                logger.error(
                    "❗ BUG: Password validation is inconsistent — login accepts temporary password but change does not.")
                assert False, "❌ ERROR: No error message shown, password change unexpectedly passed!"



        except AssertionError as ae:
            logger.error(f"❌ Test failed: {ae}")
            raise

        except Exception as e:
            logger.exception("💥 Unexpected exception occurred during password change test.")
            raise

    # After login We test the AI input under Shadow-root
    def test_AI_shadows_root(self):
        new_url = "https://web.morningexpert.com/#"
        self.driver.get(new_url)
        time.sleep(1)
        login_web_app = self.driver.find_element(By.XPATH, "//a[@id='loginButton' and (text())='Login']")
        login_web_app.click()
        time.sleep(2)
        __username = 'kalinbobchev@gmail.com'
        __password = 'gnBcvT%4ChZJ'
        self.driver.find_element(By.XPATH,
                                 '//*[@id="my-login-screen"]/div/div/div/form/ul/li[1]/div/div/div[2]/input').send_keys(
            __username)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="my-login-screen"]/div/div/div/form/ul/li[2]/div/div/div/div/div[2]/input').send_keys(
            __password)
        time.sleep(2)
        elements = self.driver.find_elements(By.XPATH, "//*[@id='loginButton']")
        elements[1].click()
        time.sleep(2)
        chat_tab = self.driver.find_element(By.XPATH, '//*[@id="chat-tab"]')
        chat_tab.click()
        time.sleep(4)
        shadow_host = self.driver.find_element(By.CSS_SELECTOR, 'deep-chat')
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        #text_input = shadow_root.find_element(By.CSS_SELECTOR, '#text-input')
        text_input = self.driver.execute_script('return arguments[0].shadowRoot.querySelector("#text-input")',
                                                shadow_host)
        text_input.send_keys('resent news')
        #submit_btn = shadow_root.find_element(By.CSS_SELECTOR, '#submit-icon')
        submit_btn = self.driver.execute_script('return arguments[0].shadowRoot.querySelector("#submit-icon")',
                                                shadow_host)
        submit_btn.click()
        time.sleep(10)
        #ai_answer = shadow_root.find_element(By.XPATH, '//*[@id="messages"]/div[3]/div/div[2]')


        ai_answer = self.driver.execute_script(
            'return arguments[0].shadowRoot.querySelector("#messages > div:nth-child(3) > div > div:nth-child(2)")',
            shadow_host)

        assert ai_answer

    #test_AI_shadows_root()
    def test_tv_sess(self):
        new_url = "https://web.morningexpert.com/#"
        self.driver.get(new_url)
        time.sleep(1)
        login_web_app = self.driver.find_element(By.XPATH, "//a[@id='loginButton' and (text())='Login']")
        login_web_app.click()
        time.sleep(2)
        __username = 'kalinbobchev@gmail.com'
        __password = 'gnBcvT%4ChZJ'
        self.driver.find_element(By.XPATH,
                                 '//*[@id="my-login-screen"]/div/div/div/form/ul/li[1]/div/div/div[2]/input').send_keys(
            __username)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="my-login-screen"]/div/div/div/form/ul/li[2]/div/div/div/div/div[2]/input').send_keys(
            __password)
        time.sleep(2)
        elements = self.driver.find_elements(By.XPATH, "//*[@id='loginButton']")
        elements[1].click()
        self.driver.find_element(By.XPATH, '//*[@id="tv-tab"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="tv"]/div[1]/div[2]/div[3]/div/div/a[3]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="tab-tv"]/div[2]/ul/div[2]/div').click()
        time.sleep(4)




    def finish_testing(self):
        self.driver.quit()

