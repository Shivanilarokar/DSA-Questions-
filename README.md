```markdown
# DSA Questions Repository 🤖

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-) ![GitHub contributors](https://img.shields.io/github/contributors/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

## Overview 🚀
This repository is aimed at aspiring developers and students who wish to enhance their understanding of data structures and algorithms through hands-on problem-solving.

## Features 🌟
- A variety of DSA questions covering multiple topics.
- In-depth explanations and code snippets for each challenge.
- Easy navigation and structure for efficient learning.
- Contributions are welcome to expand the collection.

## Summary of the Changes ⚡
Recent updates to the `README.md` include:
- Changed the title emoji for better representation.
- Minor adjustments to the structure for clarity.
- Added a note encouraging contributions to expand the collection.
- Introduced an **Example Question** section to illustrate how challenges are structured.

## Installation 🔧
To get started, clone the repository using:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-.git
```

## Usage 📖
To use the resources in this repository, navigate through the directories and choose the problems that interest you. You can also contribute by adding your own questions or improving existing ones.

## Example Question 💡
Here's an example of how challenges are structured:

### Problem: Two Sum
**Description:** Given an array of integers, return indices of the two numbers such that they add up to a specific target.

**Example:**
```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

Feel free to explore and contribute! 😊
```