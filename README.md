```markdown
# DSA Questions Repository 📖

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-)
![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social)

Welcome to the DSA Questions Repository! This repository features a collection of Data Structures and Algorithms (DSA) challenges designed to help you practice coding and improve your understanding of algorithms and data structures.

## Features ✨
- A wide variety of DSA problems to solve.
- Clear explanations and structured code examples.
- Continuous updates and contributions.

## Summary of the Changes 📲
In the latest commit, the `README.md` file has been updated to enhance the presentation and provide additional visual appeal. Notable changes include:
- The title emoji has been changed from 🤖 to 📖.
- Two badges have been added to display the repository size and the number of stars.

## Installation 🚀
To get started with this repository, clone it to your local machine:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

Once cloned, navigate to the repository directory and explore the various DSA challenges.

## Usage 🚀
You can start solving problems by navigating through the provided challenges. Each challenge is structured to help you practice and implement different data structures and algorithms.

## Example ✨
Here’s a quick example of a DSA challenge:

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

Happy coding! 🎉
```