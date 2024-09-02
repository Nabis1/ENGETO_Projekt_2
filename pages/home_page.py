from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://engeto.cz/'

    def navigate(self):
        self.page.goto(self.url)

    def accept_cookies(self, locator: str = '#cookiescript_accept'):
        accept_cookies_button = self.page.locator(locator)
        if accept_cookies_button.is_visible():
            accept_cookies_button.click()

    