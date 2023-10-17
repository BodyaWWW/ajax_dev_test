from .page import Page
from selenium.webdriver.common.by import By
import urllib.request
from bs4 import BeautifulSoup

class LoginPage(Page):

    USERNAME_INPUT = (By.ID, 'username_id')
    PASSWORD_INPUT = (By.ID, 'password_id')
    LOGIN_BUTTON = (By.ID, 'login_button_id')
    SUCCESS_MESSAGE = (By.ID, 'success_message_id')
    ERROR_MESSAGE = (By.ID, 'error_message_id')

    def try_to_enter_username(self, username):
        username_element = self.find_element(*self.USERNAME_INPUT)
        username_element.clear()
        username_element.send_keys(username)

    def try_to_enter_password(self, password):
        password_element = self.find_element(*self.PASSWORD_INPUT)
        password_element.clear()
        password_element.send_keys(password)

    def click_on_login_button(self):
        login_button_element = self.find_element(*self.LOGIN_BUTTON)
        login_button_element.click()

    def ajax_systems_apk(self):
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
