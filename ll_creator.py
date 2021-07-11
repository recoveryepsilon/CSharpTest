import sys

# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        '''Constructor for new nodes
        self = instacne of the class
        data = the integer to be stored in the node'''
        self.data = data
        self.nextNode = None

# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        '''Constructor for the head node
        self = instance of the class'''
        self.head = None

    def append_node(self, data):
        '''Appends a new node to the end of the linked list
        self = instacne of the class
        data = the integer to be stored in the node'''
        new_node = Node(data)

        # Check to see if list is empty
        # & make the new node head of list if it is
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.nextNode:
            # While the next pointer does not point
            # to "None" move to next node
            last_node = last_node.nextNode
        last_node.nextNode = new_node

    def delete_node(self, key):
        '''Traverses the list and deletes the
        frist node that the key value matches
        self = instacne of the class
        key = the data value to find the node by'''
        cur_node = self.head

        # If the node is the head node
        # Check if list is empty and if the key matches
        if cur_node and cur_node.data == key:
            self.head = cur_node.nextNode
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            # While the current node's data doesn't
            # match the key move to next node
            prev = cur_node
            cur_node = cur_node.nextNode
        
        if cur_node is None:
            print (f"Error: '{key}' could not be found in list")
            return

        prev.nextNode = cur_node.nextNode
        cur_node = None

    # Utility function to print the linked LinkedList
    def printll(self):
        '''Traverses the list and displays each node and it's data
        self = instacne of the class'''
        nodeNum = 1
        cur_node = self.head

        # Check if list is empty
        if cur_node is None:
            print("No list to display")
            return

        # Traveres the list while the current node is not
        # "None" print out the Node number and it's stored data
        while cur_node:
            print(f'Node{nodeNum}:{cur_node.data}')
            cur_node = cur_node.nextNode
            nodeNum += 1

# Driver program 
if __name__ == '__main__':

    # Function to check input
    def checkInput(line):
        '''Verifies that the line contains a working command
        line = the line read from the text document'''
        if (line.startswith("i:") or line.startswith("d:")):
            if line[2:].isdecimal():
                cmd, data = line.split(':')
                if cmd == 'i':
                    llist.append_node(data)
                else:
                    llist.delete_node(data)
            else:
                print(f"Error: '{line}' is not a valid command.")

    if len(sys.argv) == 2: # Check if a filename was given
        try:
           with open(sys.argv[1], 'r') as f:
                llist = LinkedList()
                for line in f:
                    # Loop through each line of the text document & remove any
                    #  empty lines while replacing any uppercase characters
                    line = line.lower().strip()
                    if line:
                        checkInput(line)
                llist.printll()     
        except Exception:
            print(f"Error: File '{sys.argv[1]}' Does not exist")             
    else:
        print("Error: Please provide a file name as an argument.")
                