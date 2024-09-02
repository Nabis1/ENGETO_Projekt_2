import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.course_page import CoursePage




@pytest.mark.playwright
def test_to_click_course_date(page: Page):

    hp = HomePage(page)
    cp = CoursePage(page)

    hp.navigate()
    hp.accept_cookies()
    cp.click_specific_button_inside_nav_bar('Termíny')
    CoursePage(page).assert_page_url('https://engeto.cz/terminy/')

@pytest.mark.playwright
def test_click_image(page: Page):
    
    hp = HomePage(page)
    cp = CoursePage(page)

    hp.navigate()
    hp.accept_cookies()
    cp.scroll_down(400, 1000)
    cp.click_specific_banner('Tester s Pythonem')
    cp.assert_page_url('https://engeto.cz/tester-s-pythonem/')
    
@pytest.mark.playwright
def test_add_course_to_cart(page: Page):

    hp = HomePage(page)
    cp = CoursePage(page)


    hp.navigate()
    hp.accept_cookies()
    cp.scroll_down(400, 1000)
    cp.click_specific_banner('Testing Akademie')
    cp.assert_page_url('https://engeto.cz/testovani-softwaru/')

    cp.click_specific_text_in_product_box('10. 12. – 11. 03. 2025, Online', 'Detail Termínu')
    cp.click_specific_text("Přihlas se na termín")
    cp.click_specific_text('Přejít k pokladně')

    cp.fill_billing_info(
        first_name="Karel",
        last_name="Čtvrtý",
        phone="777 999 999",
        email="Karel.IV@gmail.com",
        address="Karlštejn 172",
        city="Karlštejn",
        postcode="267 18"
    )

    cp.agree_to_terms()
    cp.submit_order()