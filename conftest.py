import pytest
from selenium import webdriver

# Fixture to set up a Selenium WebDriver (you can add more options as needed)
@pytest.fixture(scope="function")
def driver(request):
    # Initialize the WebDriver (you can choose the browser and options)
    driver = webdriver.Chrome()  # Change to the appropriate WebDriver (e.g., Firefox, Edge, etc.)

    # Teardown code (quit the WebDriver after the test)
    """ def teardown():
        driver.quit()"""

    # Register the teardown code to be run after the test
    #request.addfinalizer(teardown)

    return driver
