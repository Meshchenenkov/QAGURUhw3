import pytest
from selene import browser

@pytest.fixture(scope="session")
def browser_width_height():
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    yield
    browser.quit()