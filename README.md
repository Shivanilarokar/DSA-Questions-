```markdown
# DSA Questions Repository 🧠

![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

## Overview
This repository contains a collection of Data Structures and Algorithms (DSA) questions and solutions implemented in Python. Each function is designed to help developers understand and practice algorithms efficiently.

## Features
- Comprehensive DSA problem solutions.
- Well-documented code for easy understanding.
- Examples and usage instructions provided for each function.

## Summary of the Changes
In this update, we've made minor adjustments to the README file to improve clarity and consistency:
- Adjusted the heading levels for the **Usage** section for consistency.
- Minor code refactoring in the Fibonacci function for improved readability.

## Installation 🚀
To get started with this repository, clone it to your local machine using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
cd DSA-Questions-
```

## Usage 💻
Here’s a simple example of how to use the updated Fibonacci function:

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for checking out this repository! Happy coding! 🎉
```