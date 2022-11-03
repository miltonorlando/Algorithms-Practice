# Tower of Hanoi
The Tower of Hanoi is a mathematical puzzle where we have three rods (**A**, **B**, and **C**) and **N** disks.

All of the disks are initially piled on rod **A** in decreasing order of diameter, with the smallest disk at the top. The goal of the puzzle is to transfer the complete stack to another rod (here referred to as **C**), while adhering to the following rules:
   - Only one disk can be moved at a time.
   - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack
   - A larger disk cannot be stacked on a smaller disk.

## Overview
The program **SolveHanoi.py** runs a recursive implementation of the Tower of Hanoi in python. The output of this code describes the moves to complete the puzzle. 

## Files Required:
- SolveHanoi.py
- HanoiTower.txt

## Description
**SolveHanoi.py** reads in a file named **HanoiTower.txt**

The length of the tower, as in how many elements are there, is obtained by  calling  the  **len()** function on the array that stores it. 

The Tower of Hanoi problem is one where we have a stack of discs along with two other stations 
to hold discs, that we will denote as **A**, **B**, and **C**. The top disc of the stack being the smallest and 
the bottom one being the largest with every disc from the top to bottom increasing in size. The 
goal is to move all the discs from stack **A**, where they start, over to stack **C** and have them keep 
the same form/order as in stack **A**. However, discs can only be removed from the top of a stack 
and a larger disc cannot be placed on top of a smaller disc. In order to help with solving the 
problem, there is stack space B that lies in between **A** and **C**. This stack is used to help in moving 
discs from **A** to **C** in such a way so  that  stack  **C**  ends up  looking  just like stack A did. For 
example, the problem starts out looking like this: 

<img src="https://i.imgur.com/iefhvrf.png" height="20%" width="20%" alt="Hanoi Tower Steps"/>

And should end up looking like this: 

<img src="https://i.imgur.com/ipdFP9m.png" height="20%" width="20%" alt="Hanoi Tower Steps"/>

The  input  will  be  a  set  of  numbers  always  starting  at  1  and  ascending  by  1  everytime.  The 
number 1 will represent the top of the tower, which is the smallest disc. The total number of discs that can exist, **N**, can vary in size.

This code's output outlines the steps needed to solve the puzzle.


