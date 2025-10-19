```markdown
# DSA Questions Repository

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-) ![GitHub contributors](https://img.shields.io/github/contributors/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

## Overview
Welcome to the DSA Questions repository! This repository contains a collection of data structures and algorithms questions designed to help you practice and enhance your coding skills.

## Features
- Extensive collection of DSA questions.
- Community-driven contributions.

## Summary of the Changes
In this update, the following changes were made:
- Improved the wording in the features section for clarity.
- Separated the usage instructions into its own section for better organization.
- Enhanced the Fibonacci function example to clarify its output.

## Installation
To get started with this repository, clone it to your local machine using the following command:
```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
To use the Fibonacci function, simply call it with the desired number as shown below:

```python
def fibonacci(n):
    """Return a list of Fibonacci numbers up to n."""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Contributing
We welcome contributions! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy Coding! 🚀
```