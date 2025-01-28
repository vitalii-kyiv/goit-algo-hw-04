import random
import timeit


random_list = [random.randint(0, 5000) for _ in range(100)]


def sort_sorted():
    sorted(random_list)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def sort_merge():
     merge_sort(random_list.copy())


def insertion_sort(lst):
    for i in range(1, len(lst)): 
        key = lst[i]  
        j = i - 1  
        while j >= 0 and key < lst[j]:  
            lst[j + 1] = lst[j]  
            j -= 1  
        lst[j + 1] = key 
    return lst  

def sort_insertion():
    insertion_sort(random_list.copy())


execution_time_sorted = timeit.timeit(sort_sorted, number=1000)
execution_time_merge = timeit.timeit(sort_merge, number=1000)
execution_time_insertion = timeit.timeit(sort_insertion, number=1000)

print(f"Час сортування через built-in sorted(): {execution_time_sorted:.6f} секунд")
print(f"Час сортування через merge_sort: {execution_time_merge:.6f} секунд")
print(f"Час сортування через insertion_sort: {execution_time_insertion:.6f} секунд")
