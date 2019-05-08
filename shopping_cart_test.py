import pytest

from shopping_cart import to_usd


def test_to_usd():
    # dollar sign display
    assert to_usd(2.34) == "$2.34"

    # display two decimal places
    assert to_usd(2.3) == "$2.30"

    # display a thousands separators
    assert to_usd(23456789.3333) == "$23,456,789.33"