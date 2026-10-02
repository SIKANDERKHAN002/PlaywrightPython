import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print("This is login by email test")

@pytest.mark.sanity
def test_loginbyfacebook():
    print("This is login by facebook")
    assert 1==1

@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyphone():
    print("This is login by phone ")
    assert 1==1

@pytest.mark.sanity
def test_signupbyemail():
    print("This is signup by email test")
    assert True==True

@pytest.mark.sanity
def test_signupbyfacebok():
    print("This is signup by facebook")
    assert 1==1


@pytest.mark.skip
@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyphone():
    print("This is phone signup")
    assert 1==1