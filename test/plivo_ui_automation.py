import re
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import config as cc


class Homepage(unittest.TestCase):
    def __init__(self, testname):
        super(Homepage, self).__init__(testname)

        self.base_url = cc.BASE_URL

        print "base url ", self.base_url

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/abhi001/chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1440, 1064)
        self.base_url = self.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.status = {}


    def test_homepage(self):
        print "start"
        driver = self.driver
        driver.get(self.base_url)

        #check base url title and some more assertion check
        print driver.title

        self.assertEqual('Login :: Plum Fuse', driver.title)

        home_page = self.driver.find_element_by_xpath(
            '//*[@id="login-layout"]/div[3]/div/div[1]/div')
        print home_page.text
        self.assertEqual("Login to Plum Fuse", home_page.text)

        # click to create app button and some assertion check
        driver.find_element_by_xpath('//*[@id="link-create"]').click()

        second_screen_1 = driver.find_element_by_xpath('//*[@id="intro-dialog"]/h2')
        print second_screen_1.text
        self.assertEqual("Three easy steps and you've made your first app.", second_screen_1.text)

        second_screen_2 = driver.find_element_by_xpath('//*[@id="intro-dialog-cont"]/div[2]/button')
        print second_screen_2.text
        self.assertEqual("Let's get started!", second_screen_2.text)

        # click on Let's get started button
        driver.find_element_by_xpath('//*[@id="intro-dialog-cont"]/div[2]/button').click()
        time.sleep(4)

        #click on new page and some assertion check
        third_screen = self.driver.find_element_by_xpath('//*[@id="add-page"]')
        print third_screen.text
        self.assertEqual('New page', third_screen.text)

        #click on create new page
        driver.find_element_by_xpath('//*[@id="add-page"]').click()

        dialog_box = driver.find_element_by_xpath('//*[@id="create-dialog"]/form/p/label')
        print dialog_box.text
        self.assertEqual('Enter a new name for this page:', dialog_box.text)

        # here send the name of page to create and create page
        driver.find_element_by_xpath('//*[@id="create-dialog"]/form/p/input').send_keys(cc.NEW_PAGE_NAME)
        driver.find_element_by_xpath('/html/body/div[20]/div[3]/button[1]').click()

        # click to messaging component on the left module
        driver.find_element_by_xpath('//*[@id="accordion"]/h3[4]/a').click()
        time.sleep(4)

        # drag send an email componet from left module and palce the require position
        drag_send_sms = driver.find_element_by_xpath('//*[@id="accordion"]/div[4]/ul/li[3]')
        ActionChains(driver).drag_and_drop_by_offset(drag_send_sms, 690, 30).perform()

        # here connector connect to the start and send sms
        start_point = driver.find_element_by_xpath('//div[@id="tabs-2"]/div[2]/div[5]/div')
        sms_point = driver.find_element_by_xpath('//div[@id="tabs-2"]/div[3]/div[2]/div')
        ActionChains(driver).drag_and_drop(start_point, sms_point).perform()

        #fill the send sms required field
        driver.find_element_by_xpath('//*[@id="module-2"]/div[1]/div[3]/div/div[1]/div[2]/textarea').clear()
        driver.find_element_by_xpath('//*[@id="module-2"]/div[1]/div[3]/div/div[1]/div[2]/textarea').send_keys(cc.PHONE_NUMBER)
        driver.find_element_by_xpath('//*[@id="module-2"]/div[1]/div[3]/div/div[2]/div/table/tbody/tr/td[1]/div/textarea').clear()
        driver.find_element_by_xpath('//*[@id="module-2"]/div[1]/div[3]/div/div[2]/div/table/tbody/tr/td[1]/div/textarea').send_keys(cc.TEXT_MASSAGE)
        time.sleep(3)

        #drag send an email componet from left module and palce the require position
        drag_send_email = driver.find_element_by_xpath('//*[@id="accordion"]/div[4]/ul/li[2]')
        ActionChains(driver).drag_and_drop_by_offset(drag_send_email, 1000, 170).perform()

        # fill the required field
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[1]/div[1]/div[2]/input').send_keys(cc.SMTP_HOST)
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[1]/div[2]/div[2]/input').send_keys(cc.PORT)
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[1]/div[3]/div[2]/input').send_keys(cc.USERNAME)
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[1]/div[4]/div[2]/input').send_keys(cc.PASSWORD)
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/textarea').send_keys(cc.EMAIL_FROM)
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/textarea').send_keys(cc.EMAIL_TO)
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/textarea').send_keys(cc.SUBJECT)
        driver.find_element_by_xpath('//*[@id="module-3"]/div[1]/div[3]/div/div[3]/div/div/table/tbody/tr/td[1]/div/textarea').send_keys(cc.EMAIL_MESSAGE)

        # here connector connect from not sent output port to send an email start
        not_sent_email_source = driver.find_element_by_xpath('//div[@id="module-2"]/div/div[3]/div/div[3]/div[2]')
        start_send_email = driver.find_element_by_xpath('//div[@id="module-3"]/div[2]/div')
        ActionChains(driver).drag_and_drop(not_sent_email_source, start_send_email).perform()

        # click to basic component on the left module
        driver.find_element_by_xpath('//*[@id="accordion"]/h3[1]').click()

        # drag exit app_1 componet from left module and palce the require position
        source_exit_app_1 = driver.find_element_by_xpath('//*[@id="accordion"]/div[1]/ul/li[1]')
        ActionChains(driver).drag_and_drop_by_offset(source_exit_app_1, 420, 300).perform()

        # here connector connect from sent sms to exit_app_1
        sent_sms_source = driver.find_element_by_xpath('//div[@id="module-2"]/div/div[3]/div/div[3]/div[1]')
        exit_app_1 = driver.find_element_by_xpath('//div[@id="module-4"]/div[2]/div[1]')
        ActionChains(driver).drag_and_drop(sent_sms_source, exit_app_1).perform()

        # drag exit app_2 componet from left module and palce the require position
        ActionChains(driver).drag_and_drop_by_offset(source_exit_app_1, 540, 450).perform()

        # here connector connect from sent email to exit_app_2
        sent_email = driver.find_element_by_xpath('//div[@id="module-3"]/div/div[3]/div/div[4]/div[1]')
        exit_app_2 = driver.find_element_by_xpath('//div[@id="module-5"]/div[2]/div[1]')
        ActionChains(driver).drag_and_drop(sent_email, exit_app_2).perform()

        # drag exit app_3 componet from left module and palce the require position
        ActionChains(driver).drag_and_drop_by_offset(source_exit_app_1, 1290, 410).perform()

        # here connector connect from not sent email to exit_app_3
        not_sent_email = driver.find_element_by_xpath('//div[@id="module-3"]/div/div[3]/div/div[4]/div[2]')
        exit_app_3 = driver.find_element_by_xpath('//div[@id="module-6"]/div[2]/div[1]')
        ActionChains(driver).drag_and_drop(not_sent_email, exit_app_3).perform()

        time.sleep(4)



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
