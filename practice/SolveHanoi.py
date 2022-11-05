"""
Milton Perez
University of South Florida
09/30/2021

This program runs a recursive implementation of the Tower of Hanoi Algorithm and the output outlines the steps needed to solve the puzzle

Project File(s) Required:
    HanoiTower.txt
"""


# Function that reads hw file to generate array for the discs in the Hanoi Tower
def read():
    file = open("HanoiTower.txt", "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew


# Recursive Hanoi Tower function
def hanoiTower(discs, A, B, C):
    # Moves disc 1 from initial state to final state
    if discs == 1:
        print("Disk 1 moved from", A, "to", C)
        return
    # Calls hanoiTower function within itself
    hanoiTower(discs - 1, A, C, B)
    print("Disk", discs, "moved from", A, "to", C)
    # Calls hanoiTower function again within itself to continue until all discs are moved to their final destination C
    hanoiTower(discs - 1, B, A, C)


# Calls read function and assigns Hanoi Tower values to an array
tower = read()
# Calls hanoiTower function with the number of discs in the array, and locations A, B, & C
hanoiTower(len(tower), 'A', 'B', 'C')
