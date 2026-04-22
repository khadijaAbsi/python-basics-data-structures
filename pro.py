# Import module hello
import hello
import math
content = dir(math)
print(content)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print("*********************************************")
def mult3(n):
    result = 0
    for _ in range(n):
        result += 3
    return result

print(mult3(5))
hello.print_func1("Python")
hello.print_func2("Python")
print("*********************************************")
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print(a.pop())
print(a)
print("*********************************************")
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)
print("*********************************************")
from collections import deque
queue = deque(["Mohammad", "Modallal"])
queue.append("Ahmad")
# Terry arrives
queue.append("Ali")
# Graham arrives
print(queue.popleft())
# The first to arrive now leaves
print(queue.popleft())
# The second to arrive now leaves
print(queue)
# Remaining queue in order of
print(list(queue))
print("*********************************************")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# show that duplicates have been removed
print('orange' in basket)
# fast membership testing
print('crabgrass' in basket)
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)
# unique letters in a
print(a-b)
# letters in a but not in b
print(a|b)
# letters in either a or b
print(a&b)
# letters in both a and b
print(a^b)
# letters in a or b but not both
print("*********************************************")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'Mohammad','code':6734, 'dept': 'sales'}
print(dict['one']) # Prints value for 'one' key
print(dict[2]) # Prints value for 2 key
print(tinydict) # Prints complete dictionary
print(tinydict.keys()) # Prints all the keys
print(tinydict.values()) # Prints all the values
print("*********************************************")
def mergeSort(alist):
 print("Splitting ",alist)
 if len(alist)>1:
 mid = len(alist)//2
 lefthalf = alist[:mid]
 righthalf = alist[mid:]
 mergeSort(lefthalf)
 mergeSort(righthalf)
 i=0
 j=0
 k=0
 while i < len(lefthalf) and j < len(righthalf):
 if lefthalf[i] < righthalf[j]:
 alist[k]=lefthalf[i]
 i=i+1
 else:
 alist[k]=righthalf[j]
 j=j+1
 k=k+1
 while i < len(lefthalf):
 alist[k]=lefthalf[i]
 i=i+1
 k=k+1
 while j < len(righthalf):
 alist[k]=righthalf[j]
 j=j+1
 k=k+1
 print("Merging ",alist)
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
print("*********************************************")