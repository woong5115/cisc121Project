# cisc121Project

# Algorithm Name
Binary Search Simulator 

## Demo video/gif/screenshot of test

uploaded via OnQ


## Problem Breakdown & Computational Thinking (You can add a flowchart , write the four pillars of computational thinking briefly in bullets, etc.)

This project implements Binary Search, a classic searching algorithm used to efficiently find a target value in a sorted list. It runs in O(log n) time by repeatedly dividing the search interval in half.

1. Decomposition

Binary Search can be broken down into the following steps:

Take a sorted list and a target value.

Start with two pointers: left at the start, right at the end.

Repeatedly choose the midpoint index mid = (left + right) // 2.

Compare the middle value with the target:

If equal → found.

If smaller → search the right half.

If larger → search the left half.

Stop when left > right.

My program also:

Checks if the list is sorted.

Finds all duplicate occurrences of the target.

2. Pattern Recognition

Binary Search repeatedly:

Divides the list in half.

Compares the target to the middle element.
This repeated “halving” pattern is what makes binary search extremely efficient.

3. Abstraction

To keep the app simple for beginners:

Users only need to enter a sorted, comma-separated list.

The internal logic (midpoint calculation, pointer adjustments, duplicate scanning) is abstracted away.

Output shows each step in plain English to help users learn the algorithm.

4. Algorithm Design (Flow)

Input:
Sorted list of integers, target integer.

Process:

Validate inputs

Check sorting

Perform binary search

Scan left/right for duplicates

Generate step-by-step explanation

Output:
A clear, line-by-line explanation of the binary search process.

Algorithm & Code Explanation

My implementation includes:

Input validation

A helper function is_sorted()

A fully step-by-step interactive binary search

Duplicate detection

A Gradio-based user interface

## Steps to Run
1. go to the hugface app and find andrew543/cisc121Project from spaces or follow the link below.

2. put sorted array. comma will seperate each element of array.

3. put the number you want to find

4. result will pop up right side.



Hugging Face Link

https://huggingface.co/spaces/andrew543/cisc121Project



 Author

Andrew Oh

Acknowledgments

Gradio documentation

Course lecture notes on searching algorithms

Hugging Face Spaces deployment guide
