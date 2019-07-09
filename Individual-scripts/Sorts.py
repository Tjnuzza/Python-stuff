"""
Created on Wed Jul 19 16:28:59 2017
Catalog of sorting algorithms
@author: Tom Nuzzarello
"""

def selectionsort(arr):
    for i in range(len(arr)):
        lo = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lo]:
                lo = j
        arr[i], arr[lo] = arr[lo], arr[i]
        #End selectionsort

def insertionsort(arr):
    for i in range(len(arr)):
        val = arr[i]
        pos = i
        while pos and arr[pos-1] > val:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = val
    #End insertionsort

def bubblesort(arr):
    for k in range(len(arr), 1, -1):
        for i in range(1, k):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    #End bubblesort

def cocktailsort(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        for i in range(start, end):
            if arr[i] < arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
        end -= 1
        for i in range(end, start, -1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        start +=1
        #End while
    #End cocktailsort

def gnomesort(arr):
    i = 0
    while i < len(arr):
        if arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        else:
            i += 1
    #End Gnome Sort

def gnometeleport(arr):
    i = j = 0
    while i < len(arr):
        if i and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        else:
            if i < j:
                i = j
            i += 1
            j += 1
    #End gnometeleport

#Top down merge sort, recursive
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                #End if
            k += 1
        #End while

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        #End while

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        #End while
    #End mergesort

def heapsort(arr):
    #Even though it is in two functions, only this one needs to be named if imported
    #Convert arr to heap
    length = len(arr) - 1
    leastParent = length // 2
    for i in range(leastParent, -1, -1):
        siftdown(arr, i, length)
        
    #Flatten heap into sorted array
    for i in range(length, 0, -1):
        if arr[0] > arr[i]:
            arr[0], arr[i] = arr[i], arr[0]
            siftdown(arr, 0, i-1)
    #End heapsort

#Siftdown for heapsort algorithm
def siftdown(arr, first, last):
    largest = 2*first+1
    while largest <= last:
        if largest < last and arr[largest] < arr[largest+1]:
            largest += 1   
        if arr[largest] > arr[first]:
            arr[largest], arr[first] = arr[first], arr[largest]
            first = largest
            largest = 2*first+1    
        else:
            return
    #End siftdown

def quicksort(arr, start, end):#LR pointers
    if start < end:
        pivot = arr[start]
        left = start+1
        right = end
        done = False
        #Partition
        while not done:
            while left <= right and arr[left] <= pivot:
                left += 1
            while right >= left and arr[right] >= pivot:
                right -= 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]
            #End partition
        arr[start], arr[right] = arr[right], arr[start]
        quicksort(arr, start, right-1)
        quicksort(arr, right+1, end)
    #End quicksort

def shellsort(arr):
    gap = len(arr)//2
    while gap > 0:
        for i in range(gap, len(arr)):
            val = arr[i]
            j = i
            while j >= gap and arr[j-gap] > val:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = val
        gap //= 2
    #End shellsort

#   Bottom up merge sort, not recursive
def bottomupsort(arr):
    split = 1
    while split < len(arr):
        place = 0
        
        while place < len(arr):
            lo = place
            mid = place + split
            hi = place + 2 * split

            if mid > len(arr):
                place += 2 * split
                break
            if hi > len(arr):
                hi = len(arr)

            i = j = 0
            left = arr[lo:mid]
            right = arr[mid:hi]
            newList = []
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    newList.append(left[i])
                    i += 1
                else:
                    newList.append(right[j])
                    j+= 1

            while i < len(left):
                newList.append(left[i])
                i += 1

            while j < len(right):
                newList.append(right[j])
                j += 1

            arr[lo:hi] = newList
            place += 2 * split
        #End while
        split *= 2
    #End while
# End bottomupsort
