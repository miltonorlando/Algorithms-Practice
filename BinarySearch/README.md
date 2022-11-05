# Binary Search
**BinarySearch.py** seeks to compare binary search versus linear search.

## Overview
Two functions **linear_search()** and **binary_search()** will look for a specified number in a given sorted
list (*sortedLinearInput.txt* or *sortedBinaryInput.txt*) of distinct integers.

Then both functions receive the key (*keyLinear.txt* or *keyBinary.txt*), as a parameter indicating the specified number, to look for
and return an integer: the number of steps it took to find that number or, if that number is not found,
the number of steps until returning.

The results of both functions will the be compared to determine which algorithm is faster at performing a search.

## Project Files:
- BinarySearch.py
- sortedLinearInput.txt
- sortedBinaryInput.txt
- keyLinear.txt
- keyBinary.txt

## Description
The function **main()** firsts read ascending numbers from a file named **sortedLinearInput.txt** and also from a file called **sortedBinaryInput.txt** (both are already pre-sorted, 4096 numbers in range of 1 to 10,000). The numbers from *sortedLinearInput.txt* in one list and the numbers from *sortedBinaryInput.txt* are put into their own lists. 

Two more files, one called **keyLinear.txt**, and another, called **keyBinary.txt**, are placed into their own respective list. These files consist of 16 numbers, each number representing a number you have to search for within the arrays provided. The numbers may or may not exist in the array.

After that, each number in *keyLinear.txt* will be searched for by calling **linear_search()** back to back, and each number in *keyBinary.txt* will be searched for by calling **binary_search()** back to back. The list consisting of *sortedLinearInput.txt* and each number from *keyLinear.txt* will be sent to *linear_search()* and the list consisting of *sortedBinaryInput.txt* and each number from *keyBinary.txt* will be sent to *binary_search()*. In addition, after searching for each number the number of steps it took to find each number and the average number of steps for both linear_search and binary_search will printed out.

- **Example: linear_search(arr, 5)** would call linear_search function with the array called arr and would look for the number 5 in it. This function call will return either the number of steps to find 5, or if 5 is not there the number of steps until it realize that. This number that is returned would then print and then add with every other number to search for in *keyLinear.txt* and get the average number of steps total.
