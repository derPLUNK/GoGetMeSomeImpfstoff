from selenium import webdriver
import time


class GoGetMeSomeImpfstoff:
    def __init__(self, username, pw) -> None:
        self.driver = webdriver.Firefox()
        self.username = username
        self.pw = pw

        self.login()

    def login(self):
        self.driver.get(
            "https://termin.impfcenter-rottweil.de/impfcenter/terminbuchung/")
        self.driver.find_element_by_id("inputEmail").send_keys(self.username)
        self.driver.find_element_by_id("inputPassword").send_keys(self.pw)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/form/button").click()

        while True:
            self.check_for_vaccine()
            time.sleep(10)
            self.driver.refresh()

    def select_account(self):
        self.driver.find_element_by_xpath(
            '//*[@id="impf_registration_user"]').click()
        self.driver.find_element_by_xpath(
            f'/html/body/div[2]/form/div[1]/div/select/option[1]').click()

    def check_for_vaccine(self):
        self.select_account()
        self.driver.find_element_by_xpath(
            '//*[@id="impf_registration_datumImpfung"]').click()
        for i in range(2, 10):
            try:
                self.driver.find_element_by_xpath(
                    f'/html/body/div[2]/form/div[2]/div/select/option[{i}]').click()
                self.driver.find_element_by_xpath('//*[@id="select-time"]')
                self.get_appointment()
                time.sleep(3)
            except:
                pass

    def get_appointment(self):
        self.driver.find_element_by_xpath(
            '//*[@id="available-hours"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="impf_registration_declarationOfConsent"]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="impf_registration_submit"]').click()
        time.sleep(60)
        self.driver.quit()

        GoGetMeSomeImpfstoff(self.username, self.pw)


GoGetMeSomeImpfstoff("MAIL", "PW")
