```markdown
# DSA Questions Repository 📚

![GitHub last commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-)

## Overview
This repository contains a collection of Data Structure and Algorithm (DSA) questions along with their solutions in multiple programming languages. It is designed to be easy to navigate and contribute to.

## Features ✨
- Comprehensive list of DSA questions
- Solutions in various programming languages
- Easy to clone and explore

## Summary of the Changes
In the latest commit, the following changes were made to the `README.md` file:
- Updated the badge for the last commit to provide more relevant information.
- Improved the language and flow in the instructions for cloning and exploring the repository.
- Enhanced the example section title for better clarity.
- Minor grammatical adjustments to improve readability.

## Installation
To get started with this repository, simply clone it to your local machine:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
Explore the various DSA problems and their solutions available in this repository. You can contribute by adding more solutions or improving existing ones.

### Example
Here is an example of the Fibonacci function implemented in Python:

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Feel free to modify and enhance this function based on your understanding!

## Contributing
We welcome contributions! Please feel free to open issues or submit pull requests to help improve this repository.
```