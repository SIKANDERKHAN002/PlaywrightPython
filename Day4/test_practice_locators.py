from playwright.sync_api  import  Page,expect


def test_pw_locators(page: Page):
     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html#",wait_until="domcontentloaded")
     page.wait_for_timeout(5000)
     #page.get_by_role('textbox',name="username").fill("This is by role!")
     page.get_by_test_id('username').fill('This is by role!')
     page.get_by_role(5000)