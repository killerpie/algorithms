'''
Idea: students go arrange themselves according the height. Everyone check for themselves. nobody has to help him or show his place --> students can QUICKLY sort themselves. 
yet this is not the fastest method. 

example 1: [10,80,90,60,30,20]   surely first one is sorted because all elements on the right are larger.
example 2: [6,3,5,4,2,1,9]       surely last one is sorted because all elements on the left are smaller. 
example 3: [4,6,7,10,16,13,14,12] surely [10] is sorted because all elements are larger on its right and smaller on its left.

quick sort is a divide and conquer problem, it means it will split the problem into subproblems and sort those subproblems. 
'''

# find the position for the pivot element. start with the first in the list. 
# while i < j, find list[i] greater than pivot; find list[j] smaller than pivot. then swap. when i > j, j is where the pivot's position, swap elements of j and pivot. pivot is sorted 
# proceed to next pivot. 


# Recursive quick sort

def partition(list,start,end):
  pivot = list[start]
  i = start + 1
  j = end
  while i < j: 
    while list[i] <= pivot:
        i += 1
    while list[j] > pivot:
        j -= 1
    list[i],list[j] = list[j],list[i]
    return j


def quickSort(low,high): 
  if low < high:
    j = partition(low,high)
    quickSort(low,j)
    quickSort(j+1,high) 
    
    
    
    
    
