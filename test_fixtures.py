import pytest
from selene import browser, config

@pytest.fixture(scope="session")
def browser_width_height():
    config.window_width = 1280
    config.window_height = 1024

    yield
    browser.quit()