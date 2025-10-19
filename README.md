```markdown
# DSA Questions Repository

![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

Welcome to the DSA Questions repository! This repository contains a collection of Data Structures and Algorithms (DSA) problems designed to help you enhance your coding skills.

## Features
- A comprehensive collection of DSA problems.
- Solutions and explanations for each problem.

## Summary of the Changes
In the latest update, the `README.md` file has been improved to enhance informativeness and usability:
- **Added a section** to clarify the example usage of the Fibonacci function for better understanding.
- **Modified wording** in the installation instructions for clarity.

## Installation
To get started, clone the repository using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
Once you have cloned the repository, navigate to the directory and follow the instructions provided in the respective problem files. Here's an example of how to use the Fibonacci function:

```python
def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # Output: 3
```

Feel free to explore and contribute to the repository!
```