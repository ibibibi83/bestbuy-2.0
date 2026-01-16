"""
Unit tests for the Product class.

These tests verify correct product creation, validation,
purchase behavior, quantity reduction, and activation status.
"""

import pytest
from product import Product
from store import Store


def test_creating_product():
    """
    Tests successful creation of a Product with valid attributes.

    Verifies that name, price, quantity, and active status
    are correctly initialized.
    """
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
    """
    Tests that creating a Product with invalid details raises exceptions.

    Verifies validation for empty name and negative price.
    """
    with pytest.raises(Exception):
        Product("", price=1450, quantity=10)

    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=10)


def test_buy_reduces_quantity_and_deactivates():
    """
    Tests that buying a product reduces its quantity
    and deactivates it when quantity reaches zero.
    """
    product = Product("MacBook Air M2", price=1450, quantity=2)

    product.buy(1)
    assert product.quantity == 1
    assert product.is_active()

    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()


def test_buy_reduces_quantity_and_deactivates():
    """
    Tests that buying a product reduces its quantity
    and deactivates it when quantity reaches zero.

    This test duplicates the previous test intentionally.
    """
    product = Product("MacBook Air M2", price=1450, quantity=2)

    product.buy(1)
    assert product.quantity == 1
    assert product.is_active()

    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()

def test_print_products_outputs_correct_format(capsys):
    store = Store()
    store.add_product(Product("Laptop", 1000, 5))
    store.add_product(Product("Mouse", 50, 10))

    print_products(store)

    captured = capsys.readouterr().out
    assert "Laptop: 1000$, amount: 5" in captured
    assert "Mouse: 50$, amount: 10" in captured

def test_print_total_quantity(capsys):
    store = Store()
    store.add_product(Product("Keyboard", 80, 7))
    store.add_product(Product("Mouse", 50, 3))

    print_total_quantity(store)

    captured = capsys.readouterr().out
    assert "Total amount in store: 10" in captured

def test_command_make_order_success(monkeypatch, capsys):
    store = Store()
    store.add_product(Product("Laptop", 1000, 5))


    command_make_order(store)

    captured = capsys.readouterr().out
    assert "Total price: 2000$" in captured

    product = store.get_product_by_name("Laptop")
    assert product.quantity == 3
