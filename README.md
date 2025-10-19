```markdown
# DSA Questions Repository 🤖

Welcome to the DSA Questions repository! This project aims to provide a collection of data structures and algorithms questions along with their solutions. This repository contains implementations of various data structures and algorithms in Python. The code is designed to be well-structured and easy to understand, making it a valuable resource for learners and developers alike.

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-) ![GitHub last commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-)

## Overview

This repository offers a comprehensive collection of data structures and algorithms, complete with code examples implemented in Python. Whether you are a beginner or an experienced developer, you will find the content structured and easy to follow.

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

# Example of using the class
acc = BankAccount("Shivani", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.show_balance()
```

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements.

---

Thank you for checking out the DSA Questions repository! Happy coding! 🚀
```