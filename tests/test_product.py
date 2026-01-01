import pytest
from products import Product

def test_creating_product():
    product = Product(
        "MacBook Air M2",
        price=1450,
        quantity=10
    )

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 10
    assert product.is_active()

def test_creating_product_invalid_details():
    with pytest.raises(Exception):
        Product("", price=1450, quantity=10)

    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=10)

def test_buy_reduces_quantity_and_deactivates():
    product = Product("MacBook Air M2", price=1450, quantity=2)

    product.buy(1)
    assert product.quantity == 1
    assert product.is_active()

    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()

def test_buy_reduces_quantity_and_deactivates():
    product = Product("MacBook Air M2", price=1450, quantity=2)

    product.buy(1)
    assert product.quantity == 1
    assert product.is_active()

    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()
