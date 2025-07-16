from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


@pytest.mark.usefixtures("setup", "onetimesetup")
class MorningexpertTests:
    def prepare_and_start_testing(self):
        options = Options()
        prefs = {
            "profile.default_content_setting_values.notifications": 2  # 2 = Block
        }
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 10)
        web_url = "https://morningexpert.com/"
        self.driver.get(web_url)
        time.sleep(2)

    def youtube_testing(self):
        original_window = self.driver.current_window_handle
        first_youtube = self.driver.find_element(By.XPATH, '//*[@id="home"]/ul/li[4]/a')
        self.driver.execute_script(
            "window.open(arguments[0].href, 'https://www.youtube.com/channel/UCdXg9VKrpTDo2V5Ys-DDdOA');",
            first_youtube)
        time.sleep(3)
        self.driver.switch_to.window(original_window)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        youtube = self.driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div[1]/ul/li[4]/a')
        youtube.click()
        time.sleep(3)
        bizki = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')))
        bizki.click()
        time.sleep(8)

    def artikel_testing(self):
        self.driver.execute_script("window.scrollBy(0, 3200);")
        time.sleep(2)

        artikel_elements = self.driver.find_elements(By.XPATH, '//*[@id="about"]/div[3]/div/div/div')

        for artikel in artikel_elements:
            print(artikel.text)

        time.sleep(1)

    def test_login(self):
        new_url = "https://web.morningexpert.com/#"
        self.driver.get(new_url)
        time.sleep(2)
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
        assert elements
        time.sleep(2)

        # After login We test the AI input under Shadow-root
        def test_AI_shadows_root():
            chat_tab = self.driver.find_element(By.XPATH, '//*[@id="chat-tab"]')
            chat_tab.click()
            time.sleep(4)
            shadow_host = self.driver.find_element(By.CSS_SELECTOR, 'deep-chat')
            shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
            text_input = shadow_root.find_element(By.CSS_SELECTOR, '#text-input')
            text_input.send_keys('resent news')
            submit_btn = shadow_root.find_element(By.CSS_SELECTOR, '#submit-icon')
            submit_btn.click()
            time.sleep(10)

        #test_AI_shadows_root()
        def test_tv_sess():
            self.driver.find_element(By.XPATH, '//*[@id="tv-tab"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="tv"]/div[1]/div[2]/div[3]/div/div/a[3]').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="tab-tv"]/div[2]/ul/div[2]/div').click()
            time.sleep(4)

        #test_tv_sess()
        def test_pass_change_fail():
            self.driver.find_element(By.XPATH, '//*[@id="profile-tab"]').click()
            change_pass = self.driver.find_element(By.XPATH, '//*[@id="settings-list"]/ul/li[4]/a')
            change_pass.click()
            current_password = __password
            new_password = '4Psdfg()*__ABV'
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="oldPass"]').send_keys(current_password)
            self.driver.find_element(By.XPATH, '//*[@id="newPass"]').send_keys(new_password)
            self.driver.find_element(By.XPATH, '//*[@id="newPass2"]').send_keys(new_password)
            print('The button Change is not clickable or is overloaded or hidden')

            time.sleep(4)

            #To add logic to change new password to current password only if it works, but now the test fails.
            #This bug appiarce when using temporaly password. It works to login but you can not change it.
            # old_pass_fail = self.driver.find_element(By.XPATH, '//*[@id="changepass-form"]/div[4]/div/div/label')
            # if old_pass_fail.is_displayed():
            #     print('The old password works for the login, but here fails to the change password')
            #     return True
            # else:
            #     print('WOW, The devs from morningexpert fixed the problem with password change')
            #
            #     return False

        test_pass_change_fail()

    def finish_testing(self):
        self.driver.quit()

