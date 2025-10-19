```markdown
# 🎉 DSA Questions Repository

This repository contains a collection of Data Structures and Algorithms (DSA) questions and their respective solutions, designed to help you enhance your coding skills and understanding of fundamental concepts.

## Features
- Comprehensive set of DSA problems
- Clear and concise solutions
- Code examples illustrating usage

## Summary of the Changes
Recent updates to the `README.md` include:
- 🎉 Changed the title emoji from 🎈 to 🎉 for a more celebratory tone.
- 📜 Added an example input for the `two_sum` function to demonstrate usage clearly.
- Enhanced formatting and organization for better readability.

## Installation
To get started with this repository, clone it using the command:

```bash
git clone https://github.com/Shivanilarokar/DSA-Questions-
```

## Usage
To use the solutions provided in this repository, follow these steps:
1. Choose a problem from the repository.
2. Implement the solution in your preferred programming environment.
3. Test the solution with provided example inputs.

### Example
Here is a quick example of how to use the `two_sum` function:

```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# Example Usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]  # Because nums[0] + nums[1] == 9
```

Feel free to explore the repository and contribute by adding more questions and solutions!

## Contributing
We welcome contributions! Please fork the repository and submit a pull request for any improvements or additions.
```