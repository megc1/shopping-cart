import pytest
import datetime

from shopping_cart import to_usd, human_friendly_timestamp, find_product, calculate_total_price


def test_to_usd():
    # dollar sign display
    assert to_usd(2.34) == "$2.34"

    # display two decimal places
    assert to_usd(2.3) == "$2.30"

    # display a thousands separator
    assert to_usd(23456789.3333) == "$23,456,789.33"

def test_human_friendly_timestamp():
    now = datetime.datetime.now()
    assert "at" in human_friendly_timestamp(now)

def test_find_product():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    ]

    # return matching
    matching_product = find_product("1", products)
    assert matching_product["name"] == "Chocolate Sandwich Cookies"

    # IndexError if no match
    with pytest.raises(IndexError):
        find_product("2222", products)

def test_calculate_total_price():
    assert calculate_total_price(4) == 4.24