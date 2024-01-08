import random
import time
import matplotlib.pyplot as plt

rando_list = [random.randint(1, 10000) for i in range(100)]
sort_list = ['Bubble', 'Selection', 'Sort', 'Insertion', 'Merge', 'Quick', 'Heap', 'Shell', 'Counting', 'Radix', 'Bucket']
time_list = [0 for algorithm in sort_list]

# Bubble Sort: Complexity O(n^2)
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        if not swapped:
            return 

# Selection Sort: Complexity O(n^2)
def selectionSort(arr):
    n = len(arr)
    for ind in range(n):
        min_index = ind

        for j in range(ind + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])

# Insertion Sort: Complexity O(n^2)): 
def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Merge Sort: Complexity O(nlog(n)):  
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        mergeSort(sub_array1)
        mergeSort(sub_array2)

        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

# Quick Sort: Complexity O(nlog(n)), O(n^2) worst case:  
def quickSort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if start < end:
        p = partition(start, end)
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)

# Heap Sort: Complexity O(nlog(n)):  
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  
  
        heapify(arr, n, largest)  
def heapSort(arr):
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

# Shell Sort: Complexity O(nlog(n)) to O(nlog(n)^2):  
def shellSort(arr):
    n = len(arr)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2

# Counting Sort: Complexity O(n + k):  
def countingSort(arr):
    m = max(arr)
    count_arr = [0] * (m+1)
    for num in arr:
        count_arr[num] += 1
    for i in range(1, m + 1):
        count_arr[i] += count_arr[i-1]
    
    final_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        final_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    
    for i in range(len(arr)):
        arr[i] = final_arr[i]

# Radix Sort: Complexity O(nk):  
def radix_countingSort(arr, p):
    n = len(arr)
    result = [0] * n
    c = [0] * 10
    
    for i in range(0, n):
        index = arr[i] // p
        c[index % 10] += 1
        
    for i in range(1, 10):
        c[i] += c[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // p  
        result[c[index % 10] - 1] = arr[i]
        c[index % 10] -= 1
        i -= 1
        
    for i in range(0, n):
        arr[i] = result[i]
def radixSort(arr):
    maximum = max(arr)

    p = 1
    while maximum // p > 0:
        radix_countingSort(arr, p)
        p *= 10

# Bucket Sort: Complexity O(n + k), O(n^2) worst case:  
def bucket_insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b
def bucketSort(x):
    if not x:
        return x

    max_value = max(x)
    min_value = min(x)
    range_of_data = max_value - min_value

    slot_num = 10

    arr = [[] for _ in range(slot_num)]

    interval = range_of_data / slot_num

    if interval == 0:
        interval = 1  

    for j in x:
        index_b = int((j - min_value) / interval)
        if index_b == slot_num:  
            index_b -= 1
        arr[index_b].append(j)

    k = 0
    for i in range(slot_num):
        arr[i] = bucket_insertionSort(arr[i])
        for j in arr[i]:
            x[k] = j
            k += 1

for i, sort_function in enumerate([bubbleSort, selectionSort, insertionSort, mergeSort, quickSort, heapSort, shellSort, countingSort, radixSort, bucketSort]):
    unsorted_list = rando_list.copy()
    sorted_list = sorted(rando_list)

    start_time = time.perf_counter()
    sort_function(unsorted_list)
    time_list[i] = time.perf_counter() - start_time

    if unsorted_list != sorted_list: 
        print(f'{sort_function.__name__} failed')
    else:
        print(f'{sort_function.__name__} succeeded')

data = [[sort_list[i], time_list[i]] for i in range(len(sort_list))]

# Extracting names and times into separate lists
names = [item[0] for item in data]
times = [item[1] for item in data]

# Creating a bar graph
plt.figure(figsize=(10, 6))
plt.bar(names, times, color='blue')
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (s)')
plt.title('Comparison of Sorting Algorithm Performance')
plt.xticks(rotation=45)
plt.show()