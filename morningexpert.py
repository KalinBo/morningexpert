from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MorningexpertTests():
    def prepare_and_start_testing(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 10)
        web_url = "https://morningexpert.com/"
        self.driver.get(web_url)
        time.sleep(2)

    def youtube_testing(self):
        original_window = self.driver.current_window_handle
        first_youtube = self.driver.find_element(By.XPATH, '//*[@id="home"]/ul/li[4]/a')
        self.driver.execute_script("window.open(arguments[0].href, 'https://www.youtube.com/channel/UCdXg9VKrpTDo2V5Ys-DDdOA');", first_youtube)
        time.sleep(3)
        self.driver.switch_to.window(original_window)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        youtube = self.driver.find_element(By.XPATH, '//*[@id="top"]/footer/div[1]/div/div[1]/ul/li[4]/a')
        youtube.click()
        time.sleep(3)
        bizki = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')))
        bizki.click()
        time.sleep(8)

    def artikel_testing(self):
        self.driver.execute_script("window.scrollBy(0, 3200);")
        time.sleep(2)

        artikel_elements = self.driver.find_elements(By.XPATH, '//*[@id="about"]/div[3]/div/div/div')

        for artikel in artikel_elements:
            print(artikel.text)

        time.sleep(1)









    def finish_testing(self):
        self.driver.quit()



tests = MorningexpertTests()
tests.prepare_and_start_testing()
tests.youtube_testing()
tests.artikel_testing()
tests.finish_testing()