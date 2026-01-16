# Store Management CLI Application

This is a simple command-line store management application written in Python.
It allows users to manage products in a store, view available items, check total stock, and place orders via an interactive menu.

---

## Features

- Add products to the store
- List all available products
- Show total quantity in the store
- Buy products and calculate total price
- Basic error handling
- Interactive CLI menu

---

## Project Structure

.
├── main.py
├── store.py
├── products.py
└── README.md

---

## Requirements

- Python 3.8 or higher
- No external libraries required

---

## How to Run

python main.py

---

## Menu Options

When running the program, the following options are available:

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit

---

## Example Output

Laptop: 1000$, amount: 5
Mouse: 50$, amount: 10
Keyboard: 80$, amount: 7

---

## Description

- Products are represented by a Product class with a name, price, and quantity.
- The Store class manages all products and handles stock changes.
- Users can purchase products by name and quantity.
- The total price is calculated automatically when an order is placed.

---

## Error Handling

- Invalid menu selections show an error message
- Ordering more items than available raises an exception
- Invalid quantity input is handled safely

---

## License

This project is intended for educational purposes only.
