from playwright.sync_api import Page, expect

class CoursePage:
    def __init__(self, page: Page):
        self.page = page

    def assert_page_url(self, expected_url: str):
        expect(self.page).to_have_url(expected_url)

    def click_specific_text_in_product_box(self, h3_text: str, link_text: str):
        product_box = self.page.locator(f'.product-box:has(h3.title:has-text("{h3_text}"))')
        expect(product_box).to_be_visible()
        detail_link = product_box.locator(f'a.block-button:has-text("{link_text}")')
        expect(detail_link).to_be_visible()
        detail_link.click()

    def click_specific_text(self, button_text: str):
        button = self.page.locator(f'button:has-text("{button_text}"), a:has-text("{button_text}")')
        expect(button).to_be_visible()
        button.click()

    def click_specific_banner(self, text: str):
        banner = self.page.locator(f'a.card:has(h3.title:has-text("{text}"))')
        expect(banner).to_be_visible()
        banner.click()

    def click_specific_button_inside_nav_bar(self, text: str):
        nav_bar = self.page.locator('#top-navigation')
        nav_bar.wait_for(state='visible')
        button = nav_bar.locator(f'a.block-button:has-text("{text}")')
        expect(button).to_be_visible()
        button.click()
    
    def scroll_down(self, x: int, y: int):
        self.page.evaluate(f'window.scrollBy({x}, {y})')

    def fill_billing_info(self, first_name, last_name, phone, email, address, city, postcode):
        self.page.fill("#billing_first_name", first_name)
        self.page.fill("#billing_last_name", last_name)
        self.page.fill("#billing_phone", phone)
        self.page.fill("#billing_email", email)
        self.page.fill("#billing_address_1", address)
        self.page.fill("#billing_city", city)
        self.page.fill("#billing_postcode", postcode)    

    def fill_input_field(self, locator: str, value: str):
        input_field = self.page.locator(locator)
        expect(input_field).to_be_visible()
        input_field.fill(value)

    def agree_to_terms(self):
        self.page.locator('#terms').click()

    def submit_order(self):
        self.click_specific_text("Objednávka zavazující k platbě")