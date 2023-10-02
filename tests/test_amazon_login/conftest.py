import pytest

from steps.az_login_page_validadtions import amazon_login_validations

@pytest.fixture(scope ="session")
def az_loginpage_obj():
    return amazon_login_validations()