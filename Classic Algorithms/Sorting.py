#!/usr/bin/env python
import random
 
#Merge Sort Worst Case: O(n*Log(n))
def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
 
def mergeSort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])
    return merge(left, right)
 
#Bubble Sort Worst Case: O(n^2)
def bubbleSort(list):
  length = len(list)
  for i in xrange(0,length-1):
        for j in xrange(0,length-1):
                if list[j+1] < list[j]:
                        temp = list[j]
                        list[j] = list[j+1]
                        list[j+1] = temp
                                
        return list
 
#Insertion Sort Worst Case: O(n^2)
def insertionSort(list):
        for i in xrange(1, len(list)):
                j = i
                while j > 0 and list[j] < list[j-1]:
                        list[j-1], list[j] = list[j], list[j-1]
                        j -= 1
        return list
 
#Selection Sort Worst Case: O(n^2)
def selectionSort(list):
        for i in xrange(0, len(list)):
                min_index = i
                for j in xrange(i, len(list)):
                        if list[j] < list[min_index]:
                                min_index = j
                list[i], list[min_index] = list[min_index], list[i]
        return list
#Quick Sort Worst Case: O(n^2) (extremely Rare)
def quickSort(list):
        if len(list) <= 1:
                return list
                
        pivot = list.pop()
        less = []
        gr8t = []
        
        for i in list:
                if i <= pivot:
                        less.append(i)
                else:
                        gr8t.append(i)
                        
        return quickSort(less) + [pivot] + quickSort(gr8t)
        
#Main        
def main():
        list = random.sample(xrange(100), 50)
        print "Unsorted"
        print list
    
        print "Merge Sorted"
        print mergeSort(list)
        
        print "Bubble Sorted"
        print bubbleSort(list)
        
        print "Insertion Sorted"
        print insertionSort(list)
        
        print "Selection Sorted"
        print selectionSort(list)
        
        print "Quick Sorted"
        print quickSort(list)
 
main()