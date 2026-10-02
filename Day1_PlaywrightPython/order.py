import pytest



# @pytest.mark.order(1)
# def test_logout():
#     print("this is logout")
#
# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")
#
# @pytest.mark.order(3)
# def test_add_item():
#     print("this is add item test")



# Approach 2: Using before , after
# Approach 3 : using marker string (user defined)


@pytest.mark.order("last")
def test_checkout():
    print("this is checkout")

@pytest.mark.order()
def test_add_item():
    print("this is add item")

@pytest.mark.order("first")
def test_login():
    print("this is login test")






