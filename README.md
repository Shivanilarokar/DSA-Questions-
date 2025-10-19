```markdown
# DSA Questions 📚

![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

## Overview

This repository contains a collection of Data Structures and Algorithms (DSA) questions and solutions in Python. It serves as a useful resource for both beginners and experienced developers looking to sharpen their DSA skills.

## Features

- Comprehensive collection of DSA questions.
- Clear and structured code examples.
- Detailed explanations for each solution.

## Summary of the Changes

Recent updates to the `README.md` include:
- 📜 Enhanced the **Overview** section for better context regarding the repository.
- 📝 Included a more detailed **Example** section to illustrate the usage of the `two_sum` function.
- 🎉 Changed the title emoji for a more celebratory tone.
- 🔗 Added social media badges for stars and forks.
- 📄 Enhanced formatting and organization for better readability.

## Installation

To use the resources from this repository, simply clone it to your local machine:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage

To use the functions provided in this repository, follow these steps:

1. Navigate to the cloned directory.
2. Open the desired Python file.
3. Call the functions with the appropriate parameters.

Here's an example of how to use the `two_sum` function:

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

Feel free to explore, contribute, and enhance this repository!
```