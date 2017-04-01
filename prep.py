class Node:
	def __init__(self, x): #x is the value of the node
		self.value = x
		self.next = None

	def append(self,next_node): #next_node is a Node
		if self.next == None:
			self.next = Node(next_node) #next_node is a number
		else: #self.next points to another node - we wanna add the next_node after that node 
			self.next.append(next_node) #recursive 

	def __str__(self): #debugging
		return "the value is: " + str(self.value) + " the child is: " + str(self.next)

#test cases

# node1 = Node(3)
# node2 = Node(4)
# # node1.append(node2)
# # print node1

# node3 = Node(2)
# node3.append(node2)
# node1.append(node3)
# print node1

##Solution

def remove_duplicates(linked_list): #linked_list is a Node
	hash_table = {}
	new_linked_list = Node(linked_list.value)
	linked_list = linked_list.next

	#we cant use a for loop because it's not like an array (not iterable)
	while linked_list is not None:
		if linked_list.value not in hash_table:
			hash_table[linked_list.value] = True
			new_linked_list.append(linked_list.value)
		# else:
		# 	pass

		linked_list = linked_list.next
	return new_linked_list


def remove_duplicates2(linked_list): #linked_list is a Node
	hash_table = {}
	new_linked_list = Node(linked_list.value)

	#we cant use a for loop because it's not like an array (not iterable)
	while linked_list.next is not None:
		if linked_list.next.value not in hash_table:
			hash_table[linked_list.next.value] = True
			new_linked_list.append(linked_list.next.value)
		# else:
		# 	pass

		linked_list = linked_list.next
	return new_linked_list

#test cases
root = Node(1)
root.append(5)
root.append(5)
root.append(2)
root.append(3)
root.append(3)
print remove_duplicates(root)
print remove_duplicates2(root)


















#def remove_duplicates(linked_list):

'''
remove duplicates from an unsorted linked list 
returns linked list without duplicates 
'''

