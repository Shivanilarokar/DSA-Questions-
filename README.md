```markdown
# DSA Questions 📚

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-)
![GitHub contributors](https://img.shields.io/github/contributors/Shivanilarokar/DSA-Questions-)

This repository focuses on providing a comprehensive collection of Data Structures and Algorithms (DSA) problems, organized into various topics for easy navigation and learning.

## Features ✨
- Extensive collection of DSA problems
- Organized by topics for easy access
- Contribution guide for collaborative enhancement

## Summary of the Changes 📝
In the latest update, the following changes were made:

- Added clear installation and usage instructions to the README.
- Introduced a contribution guide to facilitate collaborative development.
- Updated the Fibonacci function to handle edge cases more effectively.

## Installation 🚀
To get started with the DSA Questions repository, clone it using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

After cloning, navigate into the directory:

```bash
cd DSA-Questions-
```

## Usage 🔧
This repository contains various functions to solve DSA problems. Each function is documented for easy understanding.

## Example
Here’s a simple example of how to use the updated Fibonacci function:

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
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Contributing 🤝
We welcome contributions! Please refer to the contribution guide for instructions on how to contribute to this repository.

Thank you for checking out DSA Questions! Happy coding! 🎉
```