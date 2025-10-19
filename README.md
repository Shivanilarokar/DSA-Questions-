```markdown
# DSA Questions 🎉

[![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social)](https://github.com/Shivanilarokar/DSA-Questions-)
[![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)](https://github.com/Shivanilarokar/DSA-Questions-)

## Overview
The DSA Questions repository contains a curated collection of data structures and algorithms questions designed to help developers enhance their problem-solving skills and prepare for technical interviews.

## Features 🎈
- Comprehensive list of coding problems categorized by data structures and algorithms.
- Clear problem statements with example solutions.
- Easy to navigate and contribute to.

## Summary of the Changes
In the latest commit, the `README.md` file has been updated to enhance clarity and organization. Key changes include:
- Updated the repository title emoji from 🎉 to 🎈 for a more festive feel.
- Improved formatting in the **Installation** and **Usage** sections for better readability.
- Added a clearer example problem structure with enhanced code snippets.

## Installation
To get started with the DSA Questions repository, clone the repository to your local machine:
```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
Navigate to the specific problem you want to solve and follow the instructions provided in the README of that problem.

## Example
Here’s a sample problem structure you might encounter:

### Problem: Two Sum

**Description:** Given an array of integers, return indices of the two numbers such that they add up to a specific target.

```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```
```python
# Example Usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]  # Because nums[0] + nums[1] == 9
```

Feel free to explore the repository, contribute, and enhance your coding skills! Happy coding! 🚀
```