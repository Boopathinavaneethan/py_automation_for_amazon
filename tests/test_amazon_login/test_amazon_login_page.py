import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
import os
from selenium import webdriver


featureFilePath = "../../feature/amazon_login.feature"

@scenario(featureFilePath, "User logs in with valid credentials")
def test_user_login_valid_creds():
    print("User logs in with valid credentials scenario is completed")


@scenario(featureFilePath, "User logs in with invalid credentials")
def test_user_login_invalid_creds():
    print("User logs in with Invalid credentials scenario is completed")

@pytest.fixture
def browser():
    # Get the current script's directory
    #script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the WebDriver executable
    #webdriver_path = os.path.join(script_dir, "webdriver", "chromedriver.exe")
    # Initialize the WebDriver using the constructed path
    #driver = webdriver.Chrome(executable_path=webdriver_path)
    driver = webdriver.Chrome()
    yield driver
    #driver.quit()


@given("User is on the Amazon.in login page")
def open_amazon_login_page(browser, az_loginpage_obj):
    az_loginpage_obj.az_login_page(browser)
    """ browser.get("https://www.amazon.in/")
    browser.find_element_by_id("nav-link-accountList-nav-line-1").click()"""


@when("User enters valid username and password")
def enter_valid_credentials(browser):
    browser.find_element_by_id("ap_email").send_keys("your_valid_email@example.com")
    browser.find_element_by_id("continue").click()
    browser.find_element_by_id("ap_password").send_keys("your_password")
    browser.find_element_by_id("signInSubmit").click()


@then("User should be logged in successfully")
def verify_login_success(browser):
    assert "Amazon.in" in browser.title


@when("User enters invalid username and password")
def enter_invalid_credentials(browser):
    browser.find_element_by_id("ap_email").send_keys("invalid_email@example.com")
    browser.find_element_by_id("continue").click()
    browser.find_element_by_id("ap_password").send_keys("invalid_password")
    browser.find_element_by_id("signInSubmit").click()


@then("User should see an error message")
def verify_error_message(browser):
    error_message = browser.find_element_by_id("auth-error-message-box")
    assert "There was a problem" in error_message.text
