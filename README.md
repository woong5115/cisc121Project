# cisc121Project
Why I Chose Binary Search

I selected Binary Search because it is one of the most efficient and foundational searching algorithms in computer science. Unlike linear search, which checks every element one by one, binary search repeatedly divides the search interval in half. This makes it significantly faster, especially for large datasets, with a time complexity of O(log n).

Binary search is also ideal for visualization because you can clearly show the algorithm narrowing down the search range step-by-step (left, right, mid). This makes it an excellent algorithm to demonstrate in an interactive Python application, fulfilling the teaching-oriented goals of this project.

Problem Breakdown & Computational Thinking
1. Decomposition

Binary Search can be broken down into small steps:

Take user input (a sorted list + a target number).

Validate inputs to ensure the list is sorted and numeric.

Set the initial search boundaries (left and right).

Repeatedly calculate the middle index (mid).

Compare the middle value with the target.

If equal → return the result.

If the middle value is too small → search the right half.

If too large → search the left half.

If the range becomes invalid → conclude the target is not found.

Display all steps back to the user.

Breaking the problem this way makes it easier to implement, test, and visualize.

2. Pattern Recognition

Binary Search uses a repeated pattern:

Look at the middle of a list.

Decide whether the target is to the left or right.

Narrow the search to that half.

Repeat this pattern until the value is found or the search ends.

This repeated halving of the search interval is the core pattern that makes binary search efficient.

3. Abstraction

To make the app simple for users:

The user only enters two things:
✔ A sorted list
✔ A target number

All internal algorithm details (mid index, half selection, comparisons) are hidden from the user until displayed as easy-to-read text steps.

The app abstracts away:

Memory management

Loop mechanics

Index calculations

Error handling

Users only see a clear explanation of each step, making the algorithm easy to learn.

4. Algorithm Design (Input → Processing → Output)

Input:

A sorted list of integers (e.g., 1, 3, 4, 7, 9)

A target integer (e.g., 7)

Processing:

Convert input into integers

Check if the list is sorted

Perform binary search:

Calculate mid

Compare mid value to target

Adjust left/right boundaries

Record each step for the user

Output:

A step-by-step explanation of the binary search process

A final message stating whether the target was found or not

This output is displayed in a Gradio textbox

This flow ensures the algorithm is both correct and easy to understand.