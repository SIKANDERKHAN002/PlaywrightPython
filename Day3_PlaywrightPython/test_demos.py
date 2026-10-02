import pytest

#Fixture : Reusable function
@pytest.fixture
def setup():
    print("This is my setup")
    print("chrome")
    yield
    print("firefox")

def test_print_hi_one(setup):
    print("Hello World One")
    print(f"I am from here {setup}")


def test_print_hi_two(setup):
    print("Hello World Two")

def test_print_hi_three(setup):
    print("Hello World Three")
