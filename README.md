```markdown
# DSA Questions 🎉

[![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social)](https://github.com/Shivanilarokar/DSA-Questions-) 
[![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)](https://github.com/Shivanilarokar/DSA-Questions-)

## Overview
This repository contains a collection of Data Structures and Algorithms (DSA) questions designed to help you enhance your coding skills and prepare for technical interviews.

## Features
- A variety of DSA questions categorized by difficulty.
- Detailed explanations and solutions for each question.
- Code snippets in Python for easy understanding and implementation.

## Summary of the Changes
Recent updates to the `README.md` include:
- 🎉 Changed the title emoji from 🎈 to 🎉 for a more celebratory tone.
- ✏️ Added an example input for the `two_sum` function to demonstrate usage clearly.

## Installation
To get started with this repository, clone it using the command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
Navigate to the directory of the cloned repository and open the relevant Python files to explore the questions and solutions provided.

## Example
Here is a quick example of how to use the `two_sum` function:

```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# Example Input
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]  # Because nums[0] + nums[1] == 9
```

Feel free to contribute to this repository by adding more questions or improving existing solutions. Happy coding! 🚀
```