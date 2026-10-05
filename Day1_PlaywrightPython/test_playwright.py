from playwright.sync_api import Page,expect

import re

def test_verify_page_url(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(15000)
     
def test_verify_page_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    page.wait_for_timeout(18000)