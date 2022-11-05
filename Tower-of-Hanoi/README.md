# Tower of Hanoi
The Tower of Hanoi is a mathematics puzzle where we have three rods (**A**, **B**, and **C**) and **N** disks. The object of the game is to move all the disks from one side to the other. This is accomplished by only moving one disk taken from the top of a stack at a time, and not placing any larger disks over smaller disks. 

## Overview
The program **SolveHanoi.py** runs a recursive implementation of the Tower of Hanoi in python. The output of this code describes the moves to complete the puzzle. 

## Project Files:
- SolveHanoi.py (main)
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

<img src="https://i.imgur.com/iefhvrf.png" height="25%" width="25%" alt="Hanoi Tower Steps"/>

And should end up looking like this: 

<img src="https://i.imgur.com/ipdFP9m.png" height="25%" width="25%" alt="Hanoi Tower Steps"/>

The  input  will  be  a  set  of  numbers  always  starting  at  1  and  ascending  by  1  everytime.  The 
number 1 will represent the top of the tower, which is the smallest disc. The total number of discs that can exist, **N**, can vary in size.

This code's output outlines the steps needed to solve the puzzle.
