```markdown
# DSA Questions 🚀

![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-) ![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-)

Welcome to the **DSA Questions** repository! This project aims to provide a comprehensive collection of data structure and algorithm challenges to enhance your understanding and skills in this crucial area of computer science.

## Features
- A wide range of data structure and algorithm problems.
- Detailed solutions provided for each problem to enhance learning.
- Easy navigation to explore different problems.

## Summary of the Changes 📜
In the latest commit, the README file has been updated to enhance its clarity and visual appeal. The following changes were made:
- Improved title emoji from 🚀 to 🌠 for better visual impact.
- Enhanced structure of the README by improving headings and formatting.
- Added badges for GitHub issues, forks, and stars for better visibility.
- Improved the structure of the example problem section by changing headings and formatting.
- Enhanced the clarity of the problem statement and example solution.

## Installation ⚙️
To get started with this repository, clone it to your local machine using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

Once you have cloned the repository, you can explore the problems and solutions.

## Example Problem
**Problem Statement**: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

**Example Solution**:

```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

Feel free to contribute to this project by submitting issues or pull requests!
```