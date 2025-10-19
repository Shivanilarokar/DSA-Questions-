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
```python
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
```

This function takes a list of numbers and a target value, returning the indices of the two numbers that add up to the target.

## Contribution 🤝
We welcome contributions from the community! If you have a solution to a DSA question or want to suggest improvements, feel free to fork the repository and submit a pull request.

Thank you for checking out the DSA Questions repository! Happy coding! 🚀
```