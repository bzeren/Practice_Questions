## MERGE SORT ##

def merge(a,b):

#merge operation: function to merge two (sorted!) arrays, a and b in to a new array "ans"

	ans = []

	while len(a) != 0 and len(b) != 0:
		if a[0] < b[0]:
			ans.append(a[0])
			a.remove(a[0])
		else:
			ans.append(b[0])
			b.remove(b[0])
	if len(a) == 0:
		ans += b
	if len(b) == 0:
		ans += a

	return ans 

## alternatively: (less runtime)

	# ans = []
	# lcounter = 0
	# rcounter = 0

	# while lcounter < len(b) and rcounter < len(a):
	# 	if a[rcounter] < b[lcounter]:
	# 		ans.append(a[rcounter])
	# 		rcounter += 1
	# 	else:
	# 		ans.append(b[lcounter])
	# 		lcounter += 1
	# if rcounter >= len(a):
	# 	ans += b[lcounter:]
	# if lcounter >= len(b):
	# 	ans += a[rcounter:] 
	# return ans 


def merge_sort(x):

#Recursively sort the first half of the input array.
#Recursively sort the second half of the input array.
#Merge two sorted sub-lists into one list.

	if len(x) == 0 or len(x) == 1:
		return x 
	else:
		mid = len(x)/2
		a = merge_sort(x[:mid]) #from the beginning till x[mid] (not including)
		b = merge_sort(x[mid:]) #from x[mid] (including) till the end 

		return merge(a,b)

## Testing

x = [19,35,42,14,27,40]
# print merge_sort(x)

#expected output = [14,19,27,35,40,42]

## Runtime = nlogn

######################################

#QUICKSORT

def quick_sort(x):

	left_array = []
	right_array = []

	count = 0

	pivot_index = len(x)/2

	if len(x) <= 1:
		return x 

	for i in range(len(x)):
		if i != pivot_index:

			count+=1

			if x[i] < x[pivot_index]:
				left_array.append(x[i])
			else:
				right_array.append(x[i])

	array_1 = quick_sort(right_array)
	array_2 = quick_sort(left_array)

	print count

	return array_2 + [x[pivot_index]] + array_1

print quick_sort(x)

##BUBBLE SORT

def swap(i,j,x):

#takes in indices i and j, in an array x, returns x with x[i] and x[j] swapped


	temp = x[i]

	x[i] = x[j]

	x[j] = temp

	return x 

#alternatively:
	
#	return x[:i] + [x[j]] + x[i+1:j] + [x[i]] + x[j+1:]

def bubble_sort(x):
	numChecks = 0
	for i in range(len(x)-1):
		j = i + 1
		while j < len(x):
			numChecks+= 1
			if x[i] > x[j]:
				x = swap(i,j,x)
			j += 1
	print "Number of checks: ", numChecks, " input size: ", len(x)
	return x

# print bubble_sort(x)


































