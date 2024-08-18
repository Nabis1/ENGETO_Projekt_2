import pytest
from playwright.sync_api import Page, expect

def navigate_to_engeto_homepage( page: Page):
    url = 'https://engeto.cz/'
    page.goto(url)
    
def accept_cookies(page : Page, locator: str = '#cookiescript_accept'):
    acceptCookiesButton = page.locator(locator)
    if acceptCookiesButton.is_visible():
        acceptCookiesButton.click()

def assert_page_url(page: Page, expected_url: str):
    expect(page).to_have_url(expected_url)

def click_element(page: Page, selector: str):
    element = page.locator(selector)
    element.click()
    
def fill_input_field(page: Page, locator: str, value: str):
    input_field = page.locator(locator)
    input_field.fill(value)

@pytest.mark.playwright
def test_to_click_course_date(page: Page):
    
    navigate_to_engeto_homepage(page)
    
    accept_cookies(page)

    courses_link = page.locator('a.block-button.type-premium.size-l.orange-link.hide-mobile')
    courses_link.click()

    assert_page_url(page, 'https://engeto.cz/terminy/' )

@pytest.mark.playwright
def test_click_image(page: Page):
    
    
    navigate_to_engeto_homepage(page)
    accept_cookies(page)

    page.evaluate('window.scrollBy(400, 1000)')
    
    click_element(page, 'img[src="https://engeto.cz/wp-content/uploads/2022/12/TopicTesting-SmallerFalse-GreyscaleFalse-SolidTrue.svg"]')
    
    assert_page_url(page, 'https://engeto.cz/testovani-softwaru/')
    

@pytest.mark.playwright
def test_add_course_to_cart(page: Page):

    navigate_to_engeto_homepage(page)
    accept_cookies(page)

    page.evaluate('window.scrollBy(400, 1000)')
    
    click_element(page, 'img[src="https://engeto.cz/wp-content/uploads/2022/12/TopicTesting-SmallerFalse-GreyscaleFalse-SolidTrue.svg"]')
    
    assert_page_url(page, 'https://engeto.cz/testovani-softwaru/')

    click_element(page, 'a[href="https://engeto.cz/product/detail-terminu-testing-akademie-10-12-2024-25-2-2025/"]')

    click_element(page, 'a.block-button.size-l.mobile-size-xl.type-premium:has-text("Přihlas se na termín")')

    click_element(page, 'a[href="https://engeto.cz/checkout/"]')

    fill_input_field(page, '#billing_first_name', 'Karel')
    fill_input_field(page, '#billing_last_name', 'Čtvrtý')
    fill_input_field(page, '#billing_phone', '777 999 999')
    fill_input_field(page, '#billing_email', 'Karel.IV@gmail.com')
    fill_input_field(page, '#billing_address_1', 'Karlštejn 172')
    fill_input_field(page, '#billing_city', 'Karlštejn')
    fill_input_field(page, '#billing_postcode', '267 18')

    click_element(page, '#terms')

    click_element(page, '#place_order')