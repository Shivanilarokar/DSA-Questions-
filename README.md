```markdown
# DSA Questions Repository

![Last Commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-) ![License](https://img.shields.io/badge/license-MIT-blue)

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
- Revised the contribution section for a more concise message.

### Code Changes
Here are some snippets showcasing the changes made:

1. **Badge Consolidation**:
   ```markdown
   ![Last Commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-) ![License](https://img.shields.io/badge/license-MIT-blue)
   ```

2. **Updated Fibonacci Function**:
   ```python
   def fibonacci(n):
       if n == 1:
           return [0]
       elif n == 2:
           return [0, 1]
       else:
           fib_sequence = fibonacci(n - 1)
           fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
           return fib_sequence
   ```

## Installation
To get started with this repository, simply clone it to your local machine:
```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
Explore the various DSA problems and their solutions available in this repository. You can contribute by adding more solutions or improving existing ones.

## Contribution
We welcome contributions! Please feel free to open issues or submit pull requests.

Thank you for checking out the DSA Questions Repository! Happy coding! 🎉
```