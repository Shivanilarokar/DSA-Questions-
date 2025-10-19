```markdown
# DSA Questions Repository 📚🤖

![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

Welcome to the DSA Questions repository! This project aims to provide a comprehensive collection of data structures and algorithms questions along with their solutions. 🚀

## Overview

This repository contains implementations of various data structures and algorithms in Python. The code is designed to be well-structured and easy to understand, making it a valuable resource for learners and developers alike.

## Features 🎉

- Implementations of various data structures such as arrays, linked lists, stacks, queues, trees, and graphs.
- Algorithms covering sorting, searching, and dynamic programming.
- Clear and concise explanations for each question and solution.

## Summary of the Changes 📝

In the latest update, the following changes were made:

1. **Updated Introduction**: Enhanced the introduction to make it more welcoming and informative.
2. **Header Update**: Changed the section title from "Summary of Changes" to "Summary of the Changes" for clarity.
3. **Removed Notebook File**: The `Day1.ipynb` file containing initial DSA questions and their explanations was removed.
4. **Improved Functionality**:
   - Enhanced the `BankAccount` class in `function.py` to handle deposits and withdrawals more effectively.
   - Added a default balance parameter to the `BankAccount` constructor.
   - Included print statements to provide feedback on deposit and withdrawal actions.
   - Enhanced error handling for insufficient funds during withdrawals.
5. **Minor Adjustments**: Made minor adjustments to improve readability and structure throughout the README.

### Code Snippet

Here's a glimpse of the updated `BankAccount` class:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: ₹{self.balance}")

    def show_balance(self):
        print(f"Account Balance for {self.owner}: ₹{self.balance}")
```

### Example Usage

Here are some snippets from the modified sections:

```python
# Example Usage
acc = BankAccount("John Doe", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.show_balance()
```

## Installation 🛠️

To get started with this repository, clone it to your local machine:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-.git
cd DSA-Questions-
```

## Usage 📖

You can use the provided implementations by importing the respective classes or functions into your own Python scripts.

Feel free to contribute to this repository by submitting issues or pull requests! Let's enhance our coding skills together! 💪

Thank you for checking out the DSA Questions repository! Happy coding! 🚀
```