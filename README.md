```markdown
# DSA Questions 🚀

![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) ![Forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

Welcome to the **DSA Questions** repository! This project serves as a platform for developers and learners to practice and enhance their skills in Data Structures and Algorithms (DSA). This repository is designed to help you improve your understanding of various data structures and algorithms through a collection of questions and solutions.

## Features
- 📚 **Comprehensive collection of DSA questions**
- ✍️ **Detailed solutions and explanations**
- 🤝 **Open for contributions from the community**

## Summary of the Changes
In the latest update, the README.md file has been improved for clarity and usability. Key changes include:
- Enhanced usage instructions for better navigation.
- Added a new example section demonstrating the Fibonacci function.
- Minor formatting adjustments for better readability.

### Code Changes
Here is an overview of the code modifications made:

1. **Fibonacci Function Update:**
   - Changed the condition for the base case in the Fibonacci function from `if n == 1:` to `if n <= 1:` to handle both base cases in a single condition.

   ```python
   def fibonacci(n):
       if n <= 1:  # Updated condition
           return 1
       else:
           return fibonacci(n - 1) + fibonacci(n - 2)
   ```

## Installation
To get started with the DSA Questions repository, clone it to your local machine using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
After cloning the repository, navigate to the project directory and run the desired algorithms or solutions as per the instructions provided within the respective files.

```bash
cd DSA-Questions-
```

## Example
Here is an example of how to use the Fibonacci function:

```python
result = fibonacci(5)
print(result)  # Output: 8
```

Feel free to explore the repository and contribute to enhancing the collection of DSA questions and solutions!
```