```markdown
# DSA Questions Repository 🚀

![Last Commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-) ![License](https://img.shields.io/badge/license-MIT-blue)

## Overview
Welcome to the DSA Questions repository! This project contains a comprehensive collection of Data Structures and Algorithms (DSA) questions along with their solutions. It aims to help developers and learners practice and enhance their problem-solving skills.

## Features
- Comprehensive collection of DSA questions and solutions.
- Easy to navigate and contribute to.
- Examples provided for better understanding of concepts.

## Summary of the Changes
In this update, several modifications were made to enhance the `README.md` file:
- Consolidated badge display for better aesthetics.
- Removed redundant instructions regarding exploring the directory.
- Updated the Fibonacci function example to improve clarity and functionality.

## Installation
To get started with the DSA Questions repository, clone the repository and navigate into the directory:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
cd DSA-Questions-
```

## Usage
You can explore the DSA questions and their solutions in the repository. Each folder contains questions categorized by topics, along with their corresponding solutions.

## Example
Here is a sample of the updated Fibonacci function for better clarity:

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Feel free to contribute to the repository by submitting pull requests with your solutions and improvements!

## Contributing
We welcome contributions! Please read our contribution guidelines before submitting your pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```