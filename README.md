```markdown
# DSA Questions 🤖

![GitHub stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-)

## Overview
Welcome to the DSA Questions repository! This project aims to provide a comprehensive collection of Data Structures and Algorithms (DSA) problems, solutions, and resources. Whether you are a beginner looking to learn or an expert aiming to refine your skills, this repository has something for everyone.

## Features
- A wide array of DSA problems categorized for easy navigation.
- Detailed solutions and explanations to help understand each problem.
- Example code snippets to illustrate the implementations.

## Summary of the Changes
Recent updates to the README.md include enhancements to clarify the project purpose and improve the code examples. Key modifications are as follows:

- Consolidated badges for GitHub stars and forks.
- Added a detailed implementation of the `binary_search` function.
- Updated the example usage section for better clarity and usability.

### Code Snippet
Here’s a quick look at the modified code snippet in the README:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
result = binary_search([1, 2, 3, 4, 5], 3)
print(f'Target found at index: {result}')  # Output: Target found at index: 2
```

## Installation
To get started with this repository, clone it to your local machine using:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-.git
```

After cloning, navigate to the project directory:

```bash
cd DSA-Questions-
```

## Usage
You can explore the various DSA problems and their solutions in the respective folders. To see the binary search in action, you can use the updated example provided above. Feel free to modify the input array or target value to test different scenarios.

---

Feel free to explore the repository and contribute to enhancing the collection of DSA problems! Happy coding! 😃
```