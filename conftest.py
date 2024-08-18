import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo= 1000)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080}  # Set the viewport size here
    )
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()