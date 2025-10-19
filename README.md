```markdown
# 🎉 DSA Questions Repository

![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

## Overview
This repository contains a collection of Data Structures and Algorithms (DSA) questions and their solutions. It is aimed at helping developers improve their coding skills and understanding of common algorithmic problems.

## Features
- Comprehensive collection of DSA questions.
- Well-structured solutions with detailed explanations.
- Easy to navigate and contribute to.

## Summary of the Changes
Recent updates to the `README.md` include:
- 🎉 Changed the title emoji for a more celebratory tone.
- 📝 Added an example input for the `two_sum` function to demonstrate usage clearly.
- ✨ Enhanced formatting and organization for better readability.
- 📱 Added social media badges for stars and forks.
- 🔍 Enhanced the overview section for clarity.

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

print(two_sum(nums, target))  # Output: [0, 1]  # Because nums[0] + nums[1] == 9
```

Feel free to explore the repository and contribute by adding more questions and solutions!

```