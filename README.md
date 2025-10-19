```markdown
# DSA Questions Repository 🤖

Welcome to the DSA Questions repository! This project aims to provide a collection of data structures and algorithms questions along with their solutions. This repository contains implementations of various data structures and algorithms in Python. The code is designed to be well-structured and easy to understand, making it a valuable resource for learners and developers alike.

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-) ![GitHub last commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-)

## Overview

This repository offers a comprehensive collection of data structures and algorithms, complete with code examples implemented in Python. Whether you are a beginner or an experienced developer, you will find the content structured and easy to follow.

## Features

- Extensive collection of data structures and algorithms
- Well-documented code examples
- Easy to understand and contribute

## Summary of Changes ⚙️

In the latest update, the following changes were made:

- Improved the `BankAccount` class in `function.py` to handle deposits and withdrawals more effectively.
- Added default balance parameter to the `BankAccount` constructor.
- Included print statements to provide feedback on deposit and withdrawal actions.
- Enhanced error handling for insufficient funds during withdrawals.

### Code Snippet

Here’s a code snippet from the newly added `function.py` file:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"Account Balance for {self.owner}: ₹{self.balance}")

# Example Usage
acc = BankAccount("John Doe", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.show_balance()
```

## Installation

To get started with this repository, clone it using:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

Then, navigate to the project directory:

```bash
cd DSA-Questions-
```

## Usage

You can use the provided implementations by importing the respective classes or functions into your own Python scripts.

---

Thank you for checking out the DSA Questions repository! Happy coding! 🚀
```