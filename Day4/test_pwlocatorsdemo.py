import time
import re

from playwright.sync_api import Page, expect

# 1) page.get_by_alt_text()
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) page.get_by_placeholder()
# 6) page.get_by_title()
# 7) page.get_by_test_id()


def test_verify_pwlocators(page: Page):
    # page.goto("https://demo.nopcommerce.com/",wait_until="domcontentloaded")
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",wait_until="domcontentloaded")
    page.wait_for_timeout(5000)  # 500 ms = 5 secs
    
    # 1) page.get_by_placeholder()
    page.get_by_placeholder("Username").fill("Admin")
    page.wait_for_timeout(5000)
    
    # 2) page.get_by_placeholder()
    page.get_by_placeholder("Password").fill("admin123")
    page.wait_for_timeout(500)
    
    # 3) page.get_by_role()
    page.get_by_role("button",name=" Login ").click()
    page.wait_for_timeout(5000)