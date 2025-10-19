```markdown
# DSA Questions Repository

Welcome to the DSA Questions repository! This repository contains a collection of data structures and algorithms questions designed to help you practice and enhance your coding skills.

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-) ![GitHub contributors](https://img.shields.io/github/contributors/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

## Features
- Extensive collection of DSA questions.
- Community-driven contributions.
- Clear and concise explanations for each question.
- Code snippets for better understanding.

## Summary of the Changes
In this update, the following changes were made:
- Improved the wording in the features section for clarity.
- Separated the usage instructions into its own section for better organization.
- Enhanced the Fibonacci function example to clarify its output.

## Installation
To get started with this repository, clone it to your local machine using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-.git
```

## Usage
Navigate into the cloned repository directory:

```bash
cd DSA-Questions-
```

You can run the Fibonacci function as follows:

```python
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[:n]

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Contributing
We welcome contributions! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy Coding! 🚀
```