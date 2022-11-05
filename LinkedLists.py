"""
Milton Perez
University of South Florida
10/25/2022

This program uses linked lists.

When a new element (value) is inserted into a list, it gets inserted into it's appropriate (sorted) position.
"""
from node import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe is not None:
        count += 1
        probe = probe.next
    return count


def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""
    # if head == None:
    # if structure is empty
    newNode = Node(newItem)
    if head is None:
        head = newNode
        return head
    # else:
    # Insert newItem in its place (ascending order)
    else:
        if head.data.lower() >= newNode.data.lower():
            newNode.next = head
            head = newNode
        else:
            curNode = head
            while curNode.next is not None and curNode.next.data.lower() < newNode.data.lower():
                nextNode = curNode.next
                curNode = nextNode
            newNode.next = curNode.next
            curNode.next = newNode
    return head


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    currentNode = head
    while currentNode is not None:
        print(currentNode.data)
        currentNode = currentNode.next


def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""

    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)

    print('The structure contains', length(head), 'items:')
    printStructure(head)


if __name__ == "__main__": main()
