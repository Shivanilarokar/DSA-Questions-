```markdown
# DSA Questions Repository

![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

Welcome to the **DSA Questions** repository! This repository contains a collection of Data Structures and Algorithms (DSA) problems designed to help you enhance your coding skills.

## Features
- A comprehensive collection of DSA problems.
- Solutions and explanations for each problem.

## Summary of Changes
In the latest update, the following changes were made to improve clarity and correctness in the README and code examples:

- **Updated Fibonacci Function**: The base case for the Fibonacci function has been modified to handle the input `0` correctly.
- **Improved Code Readability**: Enhanced the structure of the Fibonacci function for better readability and understanding.

### Code Snippet Changes
Here’s the updated implementation of the Fibonacci function in Python:

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## Installation
To get started with this repository, clone it using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
Navigate to the directory and run the desired Python script to solve specific DSA problems.

## Example
Here’s how you can use the Fibonacci function:

```python
print(fibonacci(5))  # Output: 5
```

Happy coding! 🚀
```