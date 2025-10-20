```markdown
# DSA Questions Repository 🚀

![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) 
![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

Welcome to the **DSA Questions** repository! This repository offers a comprehensive collection of data structure and algorithm problems designed to enhance your coding skills and problem-solving abilities.

## Overview
The DSA Questions repository aims to provide a wide range of algorithmic challenges that help developers practice and improve their coding proficiency. Each problem is designed to reinforce different aspects of data structures and algorithms.

## Features
- A diverse collection of DSA problems
- Code examples in Python
- Easy navigation and usage instructions
- Contribution guidelines for aspiring developers

## Summary of the Changes
In the latest commit, the README.md file has been updated to improve clarity and visual appeal. The changes include:
- Enhanced badge styles for GitHub stars and forks.
- Minor formatting adjustments for a more professional look.
- Added an emoji to encourage contributions.

### Key Changes:
```diff
-# DSA Questions Repository 🚀
+# DSA Questions Repository

-![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)
+![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-?style=social) 
+![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-?style=social)

-Feel free to explore, contribute, and enhance your coding skills with our collection of DSA questions!
+Feel free to explore, contribute, and enhance your coding skills with our collection of DSA questions! 🎉
```

## Installation
To get started with this repository, clone it to your local machine using the command:
```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
Navigate to the directory to explore the various DSA problems available. You can use the bubble sort function from this repository as follows:

```python
# Example usage
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

example_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(example_array)
print("Sorted array:", sorted_array)
```

## Contributing
Feel free to explore, contribute, and enhance your coding skills with our collection of DSA questions! 🎉

Happy coding! 💻
```