import logging

import pytest
from utils.android_utils import android_get_desired_capabilities
from appium import webdriver
from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)


def test_successful_login(user_login_fixture):

    logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

    login_page = user_login_fixture
    logging.info("Entering username and password.")
    login_page.try_to_enter_username("qa.ajax.app.automation@gmail.com")
    login_page.try_to_enter_password("qa_automation_password")
    logging.info("Clicking the login button.")
    login_page.click_on_login_button()

    assert login_page.is_user_logged_in()
    logging.info("Login successful.")

def test_wrong_password(user_login_fixture):

    login_page = user_login_fixture
    login_page.try_to_enter_username("qa.ajax.app.automation@gmail.com")
    login_page.try_to_enter_password("incorrect_password")
    login_page.click_on_login_button()


    assert login_page.is_error_message_displayed()



@pytest.mark.parametrize("username, password", [("invalid_user", "invalid_pass"), ("", "invalid_pass")])
def test_negative_login_scenarios(user_login_fixture, username, password):

    login_page = user_login_fixture
    login_page.try_to_enter_username(username)
    login_page.try_to_enter_password(password)
    login_page.click_on_login_button()


    assert login_page.is_error_message_displayed()

