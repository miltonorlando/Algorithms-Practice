"""
Milton Perez 09/20/2021

This code compares binary search against linear search

For this to run properly please be sure to have the following files in the same folder:
    sortedLinearInput.txt
    sortedBinaryInput.txt
    keyLinear.txt
    keyBinary.txt

OVERVIEW:
-Both functions linear_search() and binary_search() will look for a number in a given sorted
(sortedLinearInput or sortedBinaryInput) list of distinct integers.
-Then both functions receive the list (keyLinear or keyBinary) as a parameter as well as the number to look for
and return an integer: the number of steps it took to find that number or, if that number is not found,
the number of steps until returning.

DESCRIPTION:
-The function main() firsts read ascending numbers from a file named
“sortedLinearInput.txt” and also from a file called “sortedBinaryInput.txt” (both are
already pre-sorted, 4096 numbers in range of 1 to 10,000). The numbers from
“sortedLinearInput.txt” in one list and the numbers from “sortedBinaryInput.txt” are put into their own lists.
-Two more files, one called “keyLinear.txt”, and another, called
“keyBinary.txt”, are placed into their own respective list. These files consist of 16
numbers, each number representing a number you have to search for within the arrays
provided. The numbers may or may not exist in the array.
-After that, each number in “keyLinear.txt” will be searched for by calling
linear_search() back to back, and each number in “keyBinary.txt” will be searched for
by calling binary_search() back to back. The list consisting of
“sortedLinearInput.txt “ and each number from “keyLinear.txt” will be sent to
linear_search() and the list consisting of “sortedBinaryInput.txt“ and each number from
“keyBinary.txt” will be sent to binary_search(). In addition, after searching for each
number the number of steps it took to find each number and the average number of steps for both
linear_search and binary_search will printed out.

EX: linear_search(arr, 5) would call linear_search function with the array called
arr and would look for the number 5 in it. This function call will return either
the number of steps to find 5, or if 5 is not there the number of steps until it
realize that. This number that is returned would then print and then add with
every other number to search for in “keyLinear.txt” and get the average number
of steps total.
"""


# Used to read a file line by line
def read_input(filename):
    file = open(filename, "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew


# Used to read file key separated by spaces (' ')
def read_key(filename):
    file = open(filename, "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values


# Used to run a linear search algorithm
def linear_search(numbers, key):
    # number of steps
    num_steps = 0
    for n in range(len(numbers)):
        # increment num_steps to count iterations
        num_steps += 1
        if numbers[n] == key:
            # Returns 2 outputs: The first output is the location of the key in the input
            # The second output is the number of steps it took find the number
            return n, num_steps
    return -1, num_steps  # if key not found


# Used to run a binary search algorithm
def binary_search(numbers, key):
    # number of steps variable
    num_steps = 0
    # Starts with the entire range.
    # Creates variables for the low, middle, and high indices of the array or list being searched.
    low = 0
    mid = len(numbers) // 2
    hi = len(numbers) - 1
    # Loops until the low number passes the high
    while hi >= low:
        mid = (hi + low) // 2
        # increment num_steps to count iterations
        num_steps += 1
        # This determines whether to cut the range to the first half or second half of list,
        # unless the numbers[mid] is == key.
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            hi = mid - 1
        else:
            # Found & returns 2 outputs: The first output is the location of the key in the input
            # The second output is the number of steps it took find the number
            return mid, num_steps
    return -1, num_steps  # if key not found


# Creates main function to run and test both linear & binary search functions
def main():
    # Read input files
    linear_input = read_input("sortedLinearInput.txt")
    binary_input = read_input("sortedBinaryInput.txt")
    # Read key files
    linear_key = read_key("keyLinear.txt")
    binary_key = read_key("keyBinary.txt")

    # Generating variables to add up the total steps it takes to find each key in the input file
    # To be used in average calculation (linear & binary)
    total_linear_steps = 0
    total_binary_steps = 0

    # Runs linear search
    print("Using linear_search: ")
    for n in linear_key:
        linear_index, linear_num_steps = (linear_search(linear_input, n))
        # If key was found in linear input file
        if linear_index != -1:
            print(n, " found in ", linear_num_steps, " steps")
        # else: If key was NOT found in linear input file
        else:
            print(n, " NOT found in ", linear_num_steps, " steps")
        # Adds number of steps using linear search to total_linear_steps to be used in average calculation
        total_linear_steps += linear_num_steps

    # Runs binary search
    print("\nUsing binary_search: ")
    for n in binary_key:
        binary_index, binary_num_steps = (binary_search(binary_input, n))
        # If key was found in binary input file
        if binary_index != -1:
            print(n, " found in ", binary_num_steps, " steps")
        # else: If key was NOT found in binary input file
        else:
            print(n, " NOT found in ", binary_num_steps, " steps")
        # Adds number of steps using binary search to total_binary_steps to be used in average calculation
        total_binary_steps += binary_num_steps

    # Calculating and printing out the average number of steps for linear & binary searches [ total / len(binary_key) ]
    avg_linear_num_steps = total_linear_steps / len(linear_key)
    avg_binary_num_steps = total_binary_steps / len(binary_key)
    print("\nAverage Linear Number of Steps: ", avg_linear_num_steps)
    print("Average Binary Number of Steps: ", avg_binary_num_steps)


# Calls main function
main()
