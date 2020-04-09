#*********** 1 Create a dummy list
# a = list()
# print(a)

#*********** 2 Create a list with data
# a = ["Item_1", 2 , True, 10.5, 'Item_5']
# print(a)

#*********** 3 List inside a list, Nested list
# a = ["Poly","Michale", ["Aurthur", "Thomas", "Johny"]]
# print(a)

#*********** 4 List length & index
# a = ["Poly","Michale", ["Aurthur", "Thomas", "Johny"]]
# b = ["Poly","Michale", "Aurthur", "Thomas", "Johny"]
# length_a = len(a)
# length_b = len(b)
# print(f"Length of a is {length_a}\nLength of b is {length_b}")
# ## index starts from '0'
# ## printing list using for & while
# for x in a:
# 	print(x) # simple list print
# for x in a[2]:
# 	print(x) # simple nested list print
# i = 0
# while i<length_a:
# 	print(a[i])
# 	i = i+1
# j = 0
# while j<length_b:
# 	print(b[j])
# 	j = j +1
# print("\n List 'a' with index\n")
# i = 0
# for x in a:
# 	print(f"{i}: {a[i]}")
# 	i = i+1
# print("\n List 'b' with index\n")
# j = 0
# for y in b:
# 	print(f"{j}: {b[j]}")
# 	j = j+1
# print(a[-1])
# print(a[length_a-1])
# print(b[-1])
# print(b[length_b-1])


#********* 5 adding items to a list
# # to add a single item list.append
# a = ["one",2, 'three']
# a.append(3) # only one argument
# print(a)
# # to add multiple items
# a.extend([2,5,'eight'])
# print(a)
# # to add item in specific index
# a.insert(2,9) # 2 argument: 1st is index and 2nd is the item itself
# print(a)

#********* 6 removing items from a list
# # to remove items from specific index or the last item
# a = ["one",2, 'three','4',7,2]
# b = a
# print(a)
# a.pop()
# print(a)
# a.pop(1)
# print(a)
# # fully clearing a list to empty
# print(b)
# b.clear()
# print(b)
# # to remove a specific items of value
# c = ["one",2, 'three','4',7,2]
# print(c)
# c.remove(2) # removes the first item with value '2'
# print(c)
# c.remove(2)
# print(c)

#******** 7 index,count,sort,reverse,join
# to find the index of a specific item
# a = [1,2,3,4,5,6,1,2,3,4,5,6]
# print(a.index(5)) # shows where the first '5' is
# print(a.index(2,3)) # shows where '2' is and searching starts from index position '3'
# print(a.index(4,2,5)) # list.index(value, start, end)
# to count how many times a specific item is present there
# a = [1,1,2,3,4,5,6,1,2,3,4,5,6]
# print(a.count(2))
# print(a.count(1))
# # to sort a list in ascending order
# a = [1,2,3,4,5,6,1,2,3,4,5,6]
# print(a)
# a.sort() # sorting in ascending order
# print(a)
# a.sort(reverse=True) # sorting in descending order
# print(a)
# # to reverse a whole list without sorting
# a = [1,1,2,3,4,5,6,6]
# a.reverse()
# print(a)

#******** 8 Slicing a list
# # list[start:end:step]
# # list[start:] ---- Full list from the start point
# # list[:end] ---- list from the begining till the end
# # list[::step] --- list with specific interval
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[2:8:2])
# print(a[2:])
# print(a[:6])
# print(a[::3])

#******** 9 swapping list items
# a = ["Rancho", "Phungshukh"]
# print(a)
# a[0],a[1] = a[1], a[0]
# print(a)

#******** 10 List comprehensions 