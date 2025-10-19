```markdown
# DSA Questions Repository 🤖

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-) ![GitHub last commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-)

## Overview

Welcome to the DSA Questions repository! This project aims to provide a collection of data structures and algorithms questions along with their solutions. This repository contains implementations of various data structures and algorithms in Python. The code is designed to be well-structured and easy to understand, making it a valuable resource for learners and developers alike.

## Features

- Comprehensive coverage of data structures and algorithms 📚
- Code examples implemented in Python 🐍
- Well-structured and easy to understand 📖

## Summary of Changes ⚙️

In the latest update, the following changes were made:

1. **Updated Header**: The header for the "Summary of Changes" section was enhanced for clarity.
2. **Removed Notebook File**: The `Day1.ipynb` file was removed, which contained initial DSA questions and their explanations.
3. **Added Functionality**: Introduced a new `function.py` file that includes a class for managing a simple bank account. This class provides methods for deposit, withdrawal, and balance display.

### Code Snippet

```python
## Summary of Changes ⚙️

In the latest update, the following changes were made:
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

You can use the provided implementations by importing the respective classes or functions into your own Python scripts. Here’s an example of how to use the `BankAccount` class:

### Example Usage

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Account Balance for {self.owner}: ₹{self.balance}")

# Example of using the class
acc = BankAccount("Shivani", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.show_balance()
```

## Contribution

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements.

Thank you for checking out the DSA Questions repository! Happy coding! 🚀
```