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
    page.wait_for_selector(selector)
    element = page.locator(selector)
    expect(element).to_be_visible()
    element.click()

def click_specific_banner(page: Page, text: str):
    banner = page.locator(f'a.card:has(h3.title:has-text("{text}"))')
    expect(banner).to_be_visible()
    banner.click()

def click_specific_button_inside_nav_bar(page: Page, text: str):
    nav_bar = page.locator('#top-navigation')
    nav_bar.wait_for(state='visible')
    button = nav_bar.locator(f'a.block-button:has-text("{text}")')
    expect(button).to_be_visible()
    button.click()    

def click_specific_text(page: Page, button_text: str):
    button = page.locator(f'button:has-text("{button_text}"), a:has-text("{button_text}")')
    expect(button).to_be_visible()
    button.click()

def click_specific_text_in_product_box(page: Page, h3_text: str, link_text: str):
    product_box = page.locator(f'.product-box:has(h3.title:has-text("{h3_text}"))')
    expect(product_box).to_be_visible()
    detail_link = product_box.locator(f'a.block-button:has-text("{link_text}")')
    expect(detail_link).to_be_visible()
    detail_link.click()
    
def fill_input_field(page: Page, locator: str, value: str):
    page.wait_for_selector(locator)
    input_field = page.locator(locator)
    expect(input_field).to_be_visible()
    input_field.fill(value)

@pytest.mark.playwright
def test_to_click_course_date(page: Page):
    
    navigate_to_engeto_homepage(page)
    
    accept_cookies(page)

    click_specific_button_inside_nav_bar(page, 'Termíny')

    assert_page_url(page, 'https://engeto.cz/terminy/' )

@pytest.mark.playwright
def test_click_image(page: Page):
    
    navigate_to_engeto_homepage(page)

    accept_cookies(page)

    page.evaluate('window.scrollBy(400, 1000)')
    
    click_specific_banner(page, 'Testing Akademie')
    
    assert_page_url(page, 'https://engeto.cz/testovani-softwaru/')
    
@pytest.mark.playwright
def test_add_course_to_cart(page: Page):

    navigate_to_engeto_homepage(page)

    accept_cookies(page)

    page.evaluate('window.scrollBy(400, 1000)')
    
    click_specific_banner(page, 'Testing Akademie')
    
    assert_page_url(page, 'https://engeto.cz/testovani-softwaru/')

    click_specific_text_in_product_box(page, '10. 12. – 11. 03. 2025, Online', 'Detail Termínu')

    click_specific_text(page, "Přihlas se na termín")

    click_specific_text(page, 'Přejít k pokladně')

    fill_input_field(page, '#billing_first_name', 'Karel')
    fill_input_field(page, '#billing_last_name', 'Čtvrtý')
    fill_input_field(page, '#billing_phone', '777 999 999')
    fill_input_field(page, '#billing_email', 'Karel.IV@gmail.com')
    fill_input_field(page, '#billing_address_1', 'Karlštejn 172')
    fill_input_field(page, '#billing_city', 'Karlštejn')
    fill_input_field(page, '#billing_postcode', '267 18')

    click_element(page, '#terms')

    click_specific_text(page, "Objednávka zavazující k platbě")