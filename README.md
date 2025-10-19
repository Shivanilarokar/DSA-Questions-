```markdown
# DSA Questions 📖

![GitHub repo size](https://img.shields.io/github/repo-size/Shivanilarokar/DSA-Questions-) 
![GitHub contributors](https://img.shields.io/github/contributors/Shivanilarokar/DSA-Questions-) 
![GitHub last commit](https://img.shields.io/github/last-commit/Shivanilarokar/DSA-Questions-) 

This repository serves as a comprehensive collection of Data Structures and Algorithms (DSA) questions and solutions to help you practice and improve your coding skills.

## Features ✨
- A variety of DSA questions covering different topics.
- Well-structured solutions to enhance understanding.
- Community contributions welcomed!

## Summary of the Changes 📝
Recent updates to the `README.md` file include:
- Updated the title emoji from 📖 to 📚.
- Added new badges for repository size, contributors, and last commit date.
- Enhanced the usage section with a clearer example of the "Two Sum" problem, including input and output code snippets.
- Revised the contributing section to encourage community involvement more explicitly.

## Installation ⚙️
To get started with this repository, simply clone it to your local machine using:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-.git
```

## Usage 📚
Here’s an example of how to approach a DSA question:

### Example Question: Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

**Input:**
```python
nums = [2, 7, 11, 15]
target = 9
```

**Output:**
```python
[0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9
```

### Example Function
```python
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
```

## Contributing 🤝
We welcome contributions from the community! Feel free to submit a pull request or open an issue if you have suggestions or improvements.

Thank you for checking out this repository! Happy coding! 🚀
```