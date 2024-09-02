import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.course_page import CoursePage




@pytest.mark.playwright
def test_to_click_course_date(page: Page):

    home_page = HomePage(page)
    course_page = CoursePage(page)

    home_page.navigate()
    home_page.accept_cookies()
    course_page.click_specific_button_inside_nav_bar('Termíny')
    CoursePage(page).assert_page_url('https://engeto.cz/terminy/')

@pytest.mark.playwright
def test_click_image(page: Page):
    
    home_page = HomePage(page)
    course_page = CoursePage(page)

    home_page.navigate()
    home_page.accept_cookies()
    course_page.scroll_down(400, 1000)
    course_page.click_specific_banner('Tester s Pythonem')
    course_page.assert_page_url('https://engeto.cz/tester-s-pythonem/')
    
@pytest.mark.playwright
def test_add_course_to_cart(page: Page):

    home_page = HomePage(page)
    course_page = CoursePage(page)


    home_page.navigate()
    home_page.accept_cookies()
    course_page.scroll_down(400, 1000)
    course_page.click_specific_banner('Testing Akademie')
    course_page.assert_page_url('https://engeto.cz/testovani-softwaru/')

    course_page.click_specific_text_in_product_box('10. 12. – 11. 03. 2025, Online', 'Detail Termínu')
    course_page.click_specific_text("Přihlas se na termín")
    course_page.click_specific_text('Přejít k pokladně')

    course_page.fill_billing_info(
        first_name="Karel",
        last_name="Čtvrtý",
        phone="777 999 999",
        email="Karel.IV@gmail.com",
        address="Karlštejn 172",
        city="Karlštejn",
        postcode="267 18"
    )

    course_page.agree_to_terms()
    course_page.submit_order()