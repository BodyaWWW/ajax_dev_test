from .page import Page
from selenium.webdriver.common.by import By
import urllib.request
from bs4 import BeautifulSoup

class LoginPage(Page):
    # Локаторы элементов на странице входа
    USERNAME_INPUT = (By.ID, 'qa.ajax.app.automation@gmail.com')
    PASSWORD_INPUT = (By.ID, 'qa_automation_password')
    LOGIN_BUTTON = (By.ID, 'login_button_id')
    SUCCESS_MESSAGE = (By.ID, 'success_message_id')
    ERROR_MESSAGE = (By.ID, 'error_message_id')

    def enter_username(self, username):
        username_element = self.find_element(*self.USERNAME_INPUT)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.find_element(*self.PASSWORD_INPUT)
        password_element.clear()
        password_element.send_keys(password)

    def click_login_button(self):
        login_button_element = self.find_element(*self.LOGIN_BUTTON)
        login_button_element.click()

    def download_ajax_systems_apk(self):
        url = "https://play.google.com/store/apps/details?id=com.ajaxsystems"

        with urllib.request.urlopen(url) as response:
            page = response.read()
            soup = BeautifulSoup(page, 'html.parser')
            download_link = soup.find("a", class_="hrTbp R8zArc")["href"]

            urllib.request.urlretrieve(download_link, "Ajax_Systems.apk")

    def is_user_logged_in(self):
        try:
            self.find_element(*self.SUCCESS_MESSAGE)
            return True
        except:
            return False

    def is_error_message_displayed(self):
        try:
            self.find_element(*self.ERROR_MESSAGE)
            return True
        except:
            return False
