```markdown
# DSA Questions Repository 📚

![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

## Overview

Welcome to the DSA Questions repository! This project aims to provide a collection of data structures and algorithms questions along with their solutions. It serves as a useful resource for learners and practitioners looking to enhance their skills in programming.

## Features

- Comprehensive set of DSA questions and solutions.
- Code examples implemented in Python.
- Well-structured and easy to understand.

## Summary of Changes ⚙️

In the latest update, the following changes were made:

1. **Removed Notebook File**: The `Day1.ipynb` file was removed, which contained initial DSA questions and their explanations.
2. **Added Functionality**: Introduced a new `function.py` file that includes a class for managing a simple bank account. This class provides methods for deposit, withdrawal, and balance display.

### Code Changes

#### Removed File: `Day1.ipynb`

This file was previously used for documenting questions and code implementations. The content has been removed entirely.

#### Added File: `function.py`

```python
class BankAccount:
    """OOP example for managing a simple bank account."""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds")
        else:
            self.balance -= amount
            print(f"💵 Withdrawn: {amount}")

    def show_balance(self):
        print(f"Account Balance for {self.owner}: ₹{self.balance}")
```

## Installation

To install this project, you can clone the repository using:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
cd DSA-Questions-
```

Make sure to have Python installed on your machine to run the examples.

## Usage

You can use the `BankAccount` class to create an account and manage transactions as shown in the example above. This is a simple demonstration of Object-Oriented Programming principles applied in Python.

## Example

```python
# Create an instance of BankAccount
acc = BankAccount("Shivani", 5000)

# Perform operations
acc.deposit(1000)   # Deposited: 1000
acc.withdraw(2000)  # Withdrawn: 2000
acc.show_balance()   # Account Balance for Shivani: ₹4000
```

Feel free to explore the repository, contribute, and improve upon the existing code!
```