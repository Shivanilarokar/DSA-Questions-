```markdown
# DSA Questions Repository 📚

![GitHub Repo stars](https://img.shields.io/github/stars/Shivanilarokar/DSA-Questions-) ![GitHub forks](https://img.shields.io/github/forks/Shivanilarokar/DSA-Questions-) ![GitHub issues](https://img.shields.io/github/issues/Shivanilarokar/DSA-Questions-)

The DSA Questions repository offers a comprehensive collection of data structures and algorithms problems along with well-structured solutions.

## Features ✨

- 📖 A wide variety of data structure and algorithm problems.
- ⚙️ Well-structured solutions for each problem.
- 📑 Easy navigation and contribution guidelines.

## Summary of the Changes 💖

Recent updates to the `README.md` include:

- Improved the title for better visual appeal.
- Enhanced the section on exploring the repository and contributing solutions.
- Included an example usage of a sorting algorithm with clear code snippets.

## Installation 🖥️

To get started with the repository, clone it using the following command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

Navigate to the directory to explore the various DSA problems available. You can run the solutions in a Python environment.

## Usage 📦

Here’s an example of how to use the bubble sort function included in this repository:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Sample input
example_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(example_array)
print("Sorted array:", sorted_array)
```

## Contributing 🤝

We welcome contributions! Please read our contribution guidelines for more details on how to get involved.

---

Happy coding! 🎉
```