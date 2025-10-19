```markdown
# DSA Questions 📚

![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

## Overview
This repository contains a collection of Data Structures and Algorithms (DSA) questions, providing solutions and explanations to help you sharpen your coding skills.

## Features
- Comprehensive coverage of key DSA topics
- Code solutions with explanations
- Step-by-step instructions for usage
- Examples to illustrate implementation

## Summary of the Changes
Recent updates to the `README.md` include:
- 📖 Included a more detailed **Example** section to illustrate the usage of the `two_sum` function.
- 🎉 Changed the title emoji for a more celebratory tone.
- 🔗 Added social media badges for stars and forks.
- 📝 Enhanced formatting and organization for better readability.

## Installation
To use the resources from this repository, simply clone it to your local machine:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
To use the functions provided in this repository, follow these steps:

1. Clone the repository to your local machine.
2. Open the desired Python file.
3. Call the functions with the appropriate parameters.

### Example
Here's an example of how to use the `two_sum` function:

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]  # Because nums[0] + nums[1] == 9
```

Feel free to explore the repository, contribute, and enhance your understanding of Data Structures and Algorithms!
```