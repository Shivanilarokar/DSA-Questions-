```markdown
# DSA Questions Repository

![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

## Overview
This repository contains a collection of Data Structures and Algorithms (DSA) questions and their solutions. It is aimed at helping developers improve their coding skills and understanding of common algorithmic problems.

## Features
- Comprehensive collection of DSA questions.
- Solutions provided in Python.
- Easy to understand and follow code examples.

## Summary of the Changes
Recent updates to the `README.md` include:
- Added an **Overview** section to give a clearer context about the repository.
- Enhanced the **Usage** section with step-by-step instructions.
- Included a more detailed **Example** section to illustrate the usage of the `two_sum` function.

## Installation
To get started with this repository, clone it using the command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
To use the solutions provided in this repository, follow these steps:
1. Choose a problem from the repository.
2. Open the corresponding Python file to explore the questions and solutions provided.

### Example
Here’s how you can use the `two_sum` function:

```python
def two_sum(nums, target):
    # Example input
    nums = [2, 7, 11, 15]
    target = 9
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]  # Because nums[0] + nums[1] == 9
```

Feel free to explore the repository and contribute by adding more questions and solutions!
```