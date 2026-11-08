import os
import time

import pyotp
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("attempt", [1])
def test_github_login_with_totp(page: Page, attempt: int):
    # totp_value = pyotp.TOTP("BUGKVIPFWJMSFEDD")
    # print(f"totp_value => {totp_value}")
    username = "sikanderofficialwork1-oss" #os.environ["GITHUB_USERNAME"]
    password = "BitJoin@1@2@3" #os.environ["GITHUB_PASSWORD"]
    totp_secret = "Test" #os.environ["GITHUB_TOTP_SECRET"]

    page.goto("https://github.com/login")

    page.get_by_label("Username or email address").fill(username)
    #time.sleep(7)
    page.get_by_label("Password").fill(password)
    time.sleep(7)
    # # page.get_by_role("button", name="Sign in").click()
    # sign_in = driver.find_element(By.XPATH, "//input[@type='submit' and @name='commit' and @value='Sign in']")
    # sign_in.click()
    
    sign_in = page.locator('input[type="submit"][name="commit"][value="Sign in"]')
    expect(sign_in).to_be_visible()
    expect(sign_in).to_be_enabled()
    sign_in.click()

    #time.sleep(20)
    # GitHub may ask for another verification step on some logins.
    # Wait for the TOTP prompt and allow time for the next code if near expiry.
    code_field = page.locator('input[name="app_otp"]')
    expect(code_field).to_be_visible(timeout=20_000)

    totp_value = pyotp.TOTP("XXXXXX")
    print(f"totp_secret=> {totp_value}")
    time.sleep(3)
    if totp_value.interval - (int(time.time()) % totp_value.interval) < 3:
        time.sleep(3)
    type_otp = totp_value.now()    
    print(type(type_otp))
    print(type_otp)
    code_field.fill(totp_value.now())
    verify = page.locator('input[type="submit"][value="Verify"]')
    #expect(verify).to_be_visible()
    #expect(verify).to_be_enabled()
    #verify.click()
    time.sleep(30)
    # # Successful login normally lands on the dashboard or a redirect target.
    # expect(page).to_have_url(lambda url: "github.com" in url and "/login" not in url,
    #                          timeout=30_000)