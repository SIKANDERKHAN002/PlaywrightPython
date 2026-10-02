import pytest

# @pytest.fixture(scope="module")
# def setup():
#     print("setup environment fixture")

def test_login(setup):
    print("This is login by email test")
    assert True==True

def test_loginFacebook(setup):
    print("This is login by facebook test")
    assert True==True

def test_loginGoogle(setup):
    print("This is login by google test")
    assert True==True


