
class Node:

    def __init__(self, x):  # x is the value of the node
        self.value = x
        self.next = None

    def append(self, next_node):  # next_node is a Node
        if self.next == None:
            self.next = Node(next_node)  # next_node is a number
        else:

              # self.next points to another node - we wanna add the next_node after that node

            self.next.append(next_node)  # recursive

    def __str__(self):  # debugging
        return str(self.value) + ' ' + str(self.next)


# test cases

# node1 = Node(3)
# node2 = Node(4)
## node1.append(node2)
## print node1

# node3 = Node(2)
# node3.append(node2)
# node1.append(node3)
# print node1

##Solution

def remove_duplicates(linked_list):  # linked_list is a Node
    hash_table = {}
    new_linked_list = Node(linked_list.value)
    linked_list = linked_list.next

    # we cant use a for loop because it's not like an array (not iterable)

    while linked_list is not None:
        if linked_list.value not in hash_table:
            hash_table[linked_list.value] = True
            new_linked_list.append(linked_list.value)

        # else:
        # ....pass

        linked_list = linked_list.next
    return new_linked_list


def remove_duplicates2(linked_list):  # linked_list is a Node
    hash_table = {}
    new_linked_list = Node(linked_list.value)

    # we cant use a for loop because it's not like an array (not iterable)

    while linked_list.next is not None:
        if linked_list.next.value not in hash_table:
            hash_table[linked_list.next.value] = True
            new_linked_list.append(linked_list.next.value)

        # else:
        # ....pass

        linked_list = linked_list.next
    return new_linked_list


## In - place solution

def remove_duplicates_inplace(linked_list):

    current_linked_list = Node(linked_list.value)
    while linked_list != None:
        pointer = linked_list.next  # pointing to the first child
        while pointer != None:
            if pointer.value != linked_list.value:
                current_linked_list.append(pointer.value)
            pointer = pointer.next  # advancing the pointer
        linked_list = linked_list.next
    return current_linked_list


# test cases

root = Node(1)
root.append(5)
root.append(5)
root.append(2)
root.append(3)
root.append(3)

# print remove_duplicates(root)
# print remove_duplicates2(root)

#print remove_duplicates_inplace(root)


## Implementing a stack

class Stack:

    def __init__(self, inputs):
        self.data = inputs

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1]

    def pop(self):
        popped = self.peek()
        self.data.remove(popped)
        return popped


class Queue:

    def __init__(self, inputs):
        self.data = inputs

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[0]

    def pop(self):
        popped = self.peek()
        self.data.remove(popped)
        return popped


class Graph:

    def __init__(self, x):  # x is the value of the node
        self.value = x
        self.neighbors = []
        self.type = True  # undirected

    #Construction
    def add_neighbor(self, next_node):  # next_node is a Node
        if self.type == False:
            self.neighbors.append(next_node)  # recursive
        else:
            if next_node not in self.neighbors:
                self.neighbors.append(next_node)  # self (graph object)
                next_node.neighbors.append(self)

    #Debug
    def toStr(self, tabLevel, startSet=None):
        #Initialize the set of printed values if not already done:
        if not startSet:
            _set = set([self]) 
        else:
            _set = startSet.union([self]) # already-printed nodes + current
            
        ans = ""
        for i in range(tabLevel):
            ans+="\t"
        ans+= self.value + ' Neighbors: '   
        
        #Print neighbors recursively
        setToPrint = set(self.neighbors) - _set #neighbors that have not been printed
        if len(setToPrint) == 0:
            ans += "None!"
        else:
            ans+= "\n"
        for neighbor in setToPrint:
            a = neighbor.toStr(tabLevel+1, _set.union(setToPrint)) + "\n"
            ans+= a
        return ans

    def __str__(self): 
        return self.toStr(0)


##### Testing Graph Class #####

a = Graph('A')  # undirected by default
b = Graph('B')
c = Graph('C')
d = Graph('D')
e = Graph('E')

#Construct a Graph:
c.add_neighbor(d)
b.add_neighbor(c)
b.add_neighbor(d)
a.add_neighbor(b)

print "D: ", d
print "C: ", c
print "B: ", b
print "A: ", a

c.add_neighbor(e) #expect change to be reflected in A

print "A after adding E to C: ", a

from enum import Enum
    
class AdjacencyGraph:
    def __init__(self, A):
        self.A = A
    
    def getNeighbors(nodeIndex):
        neighbors = []
        # add all neighbors from matrix for inputted node
        return neighbors
        
    def areConnected(node1, node2): #node1, node2 indexes into A
        pass
    
    def add_neighbor(node1, node2):
        pass
        
    