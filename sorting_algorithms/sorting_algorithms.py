########################################################################################################
# Name: sorting_algorithms.py
# Description: implements merge sort, selection sort, and ;
#              tests these algorithms on arrays of different types of input.
#              Sorted data is defined as having all the values arranged from smallest to largest  
# Author: Medina Lamkin
# Last Edited: 08/02/2019
#
########################################################################################################
import numpy as np
import time
import math
################################ FUNCTIONS TO CREATE ARRAYS ############################################

#creates a 1D array with random input
def create_random(size):
    return np.random.rand(size)


#creates a 1D array with ordered input
def create_ordered(size):
    array = np.empty(size)
    for i in range(size):
        array[i] = i
        
    return array


#creates a 1D array with ordered input
def create_reverse_ordered(size):
    array = np.empty(size)
    for i in range(size):
        array[i] = size - i
        
    return array
    
    
#creates a 1D array with identical input
def create_same(size):
    return np.ones(size)


#creates a half sorted array
def create_half_sorted(size):
    array = np.random.rand(size)
    for i in range(int(size/2)):
        array[i] = i

    return array


##################################### SORTING FUNCTIONS ################################################


def insertion_sort(array):
    for i in range(1, len(array)):
        unsorted = array[i]
        
        #shift the elements
        j = i - 1
        while j >= 0 and unsorted < array[j]:
           # print(unsorted)
            array[j+1] = array[j]
            j -= 1
            
        array[j+1] = unsorted
      
      

def merge_sort(array):
    if len(array) > 1:
        arrayA = array[0:math.floor(len(array)/2)]
        arrayB = array[math.floor(len(array)/2):len(array)]
        
        merge_sort(arrayA)
        merge_sort(arrayB)
        
        return merge(arrayA, arrayB)

def merge(arrayA, arrayB):
    merged_list = [*arrayA, *arrayB]
    insertion_sort_for_merge(merged_list)
    
    return merged_list

       
def insertion_sort_for_merge(array):
    
    if len(array) == 1:
        return array
    
    for i in range(1, len(array)):
        unsorted = array[i]
        
        #shift the elements
        j = i - 1
        while j >= 0 and unsorted < array[j]:
           # print(unsorted)
            array[j+1] = array[j]
            j -= 1
            
        array[j+1] = unsorted
        
    return array



def selection_sort(array):
    for i in range(len(array)-1):
        min = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
                
        temp = array[i]
        array[i] = array[min]
        array[min] = temp


########################################## TIMING FUNCTIONS ############################################


def time_s(sorting_function, array_to_sort):
    start_time = time.process_time()
    sorting_function(array_to_sort)
    end_time = time.process_time()
    
    elapsed_time = end_time - start_time
    print ("elapsed: ", elapsed_time)
    
    
#used for functions without return values
def time_s_r(sorting_function, array_to_sort):
    start_time = time.process_time()
    return_value = sorting_function(array_to_sort)
    end_time = time.process_time()
    
    elapsed_time = end_time - start_time
    print ("elapsed: ", elapsed_time)
    
    return return_value
    
####################################### SELECTION SORT #################################################

print("1st - on random array")
print("2nd - on sorted array")
print("3rd - on reverse sorted array")
print("4th - on array with all identical items")
print("5th - on half sorted, half random array")


# With 10 elements
print()
print("Selecton sort timings on 10 elements")

array1 = create_random(10)
array2 = create_ordered(10)
array3 = create_reverse_ordered(10)
array4 = create_same(10)
array5 = create_half_sorted(10)

time_s(selection_sort, array1)
time_s(selection_sort, array2)
time_s(selection_sort, array3)
time_s(selection_sort, array4)
time_s(selection_sort, array5)


# With 100 elements
print()
print("Selecton sort timings on 100 elements")

array1 = create_random(100)
array2 = create_ordered(100)
array3 = create_reverse_ordered(100)
array4 = create_same(100)
array5 = create_half_sorted(100)

time_s(selection_sort, array1)
time_s(selection_sort, array2)
time_s(selection_sort, array3)
time_s(selection_sort, array4)
time_s(selection_sort, array5)


# With 1 000 elements
print()
print("Selecton sort timings on 1 000 elements")

array1 = create_random(1000)
array2 = create_ordered(1000)
array3 = create_reverse_ordered(1000)
array4 = create_same(1000)
array5 = create_half_sorted(1000)

time_s(selection_sort, array1)
time_s(selection_sort, array2)
time_s(selection_sort, array3)
time_s(selection_sort, array4)
time_s(selection_sort, array5)


# With 10 000 elements
print()
print("Selecton sort timings on 10 000 elements")

array1 = create_random(10000)
array2 = create_ordered(10000)
array3 = create_reverse_ordered(10000)
array4 = create_same(10000)
array5 = create_half_sorted(10000)

time_s(selection_sort, array1)
time_s(selection_sort, array2)
time_s(selection_sort, array3)
time_s(selection_sort, array4)
time_s(selection_sort, array5)


# With 100 000 elements
print()
print("Selecton sort timings on 100 000 elements")

array1 = create_random(100000)
array2 = create_ordered(100000)
array3 = create_reverse_ordered(100000)
array4 = create_same(100000)
array5 = create_half_sorted(100000)

time_s(selection_sort, array1)
time_s(selection_sort, array2)
time_s(selection_sort, array3)
time_s(selection_sort, array4)
time_s(selection_sort, array5)


######################################### MERGE SORT ###################################################

print("1st - on random array")
print("2nd - on sorted array")
print("3rd - on reverse sorted array")
print("4th - on array with all identical items")
print("5th - on half sorted, half random array")


# With 10 elements
print()
print("Merge sort timings on 10 elements")

array1 = create_random(10)
array2 = create_ordered(10)
array3 = create_reverse_ordered(10)
array4 = create_same(10)
array5 = create_half_sorted(10)

#print(array1)
#print(array2)
#print(array3)
#print(array4)
#print(array5)

array1 = time_s_r(merge_sort, array1)
array2 = time_s_r(merge_sort, array2)
array3 = time_s_r(merge_sort, array3)
array4 = time_s_r(merge_sort, array4)
array5 = time_s_r(merge_sort, array5)


# With 100 elements
print()
print("Merge sort timings on 100 elements")

array1 = create_random(100)
array2 = create_ordered(100)
array3 = create_reverse_ordered(100)
array4 = create_same(100)
array5 = create_half_sorted(100)

array1 = time_s_r(merge_sort, array1)
array2 = time_s_r(merge_sort, array2)
array3 = time_s_r(merge_sort, array3)
array4 = time_s_r(merge_sort, array4)
array5 = time_s_r(merge_sort, array5)


# With 1 000 elements
print()
print("Merge sort timings on 1 000 elements")

array1 = create_random(1000)
array2 = create_ordered(1000)
array3 = create_reverse_ordered(1000)
array4 = create_same(1000)
array5 = create_half_sorted(1000)

array1 = time_s_r(merge_sort, array1)
array2 = time_s_r(merge_sort, array2)
array3 = time_s_r(merge_sort, array3)
array4 = time_s_r(merge_sort, array4)
array5 = time_s_r(merge_sort, array5)


# With 10 000 elements
print()
print("Merge sort timings on 10 000 elements")

array1 = create_random(10000)
array2 = create_ordered(10000)
array3 = create_reverse_ordered(10000)
array4 = create_same(10000)
array5 = create_half_sorted(10000)

array1 = time_s_r(merge_sort, array1)
array2 = time_s_r(merge_sort, array2)
array3 = time_s_r(merge_sort, array3)
array4 = time_s_r(merge_sort, array4)
array5 = time_s_r(merge_sort, array5)
   
   
# With 100 000 elements
print()
print("Merge sort timings on 100 000 elements")

array1 = create_random(100000)
array2 = create_ordered(100000)
array3 = create_reverse_ordered(100000)
array4 = create_same(100000)
array5 = create_half_sorted(100000)

array1 = time_s_r(merge_sort, array1)
array2 = time_s_r(merge_sort, array2)
array3 = time_s_r(merge_sort, array3)
array4 = time_s_r(merge_sort, array4)
array5 = time_s_r(merge_sort, array5)


######################################## INSERTION SORT ################################################

"""
print("1st - on random array")
print("2nd - on sorted array")
print("3rd - on reverse sorted array")
print("4th - on array with all identical items")
print("5th - on half sorted, half random array")


# With 10 elements
print()
print("Insertions sort timings on 10 elements")

array1 = create_random(10)
array2 = create_ordered(10)
array3 = create_reverse_ordered(10)
array4 = create_same(10)
array5 = create_half_sorted(10)

time_s(insertion_sort, array1)
time_s(insertion_sort, array2)
time_s(insertion_sort, array3)
time_s(insertion_sort, array4)
time_s(insertion_sort, array5)


# With 100 elements
print()
print("Insertions sort timings on 100 elements")

array1 = create_random(100)
array2 = create_ordered(100)
array3 = create_reverse_ordered(100)
array4 = create_same(100)
array5 = create_half_sorted(100)

time_s(insertion_sort, array1)
time_s(insertion_sort, array2)
time_s(insertion_sort, array3)
time_s(insertion_sort, array4)
time_s(insertion_sort, array5)


# With 1 000 elements
print()
print("Insertions sort timings on 1 000 elements")

array1 = create_random(1000)
array2 = create_ordered(1000)
array3 = create_reverse_ordered(1000)
array4 = create_same(1000)
array5 = create_half_sorted(1000)

time_s(insertion_sort, array1)
time_s(insertion_sort, array2)
time_s(insertion_sort, array3)
time_s(insertion_sort, array4)
time_s(insertion_sort, array5)


# With 10 000 elements
print()
print("Insertions sort timings on 10 000 elements")

array1 = create_random(10000)
array2 = create_ordered(10000)
array3 = create_reverse_ordered(10000)
array4 = create_same(10000)
array5 = create_half_sorted(10000)

time_s(insertion_sort, array1)
time_s(insertion_sort, array2)
time_s(insertion_sort, array3)
time_s(insertion_sort, array4)
time_s(insertion_sort, array5)


# With 100 000 elements
print()
print("Insertions sort timings on 100 000 elements")

array1 = create_random(100000)
array2 = create_ordered(100000)
array3 = create_reverse_ordered(100000)
array4 = create_same(100000)
array5 = create_half_sorted(100000)

time_s(insertion_sort, array1)
time_s(insertion_sort, array2)
time_s(insertion_sort, array3)
time_s(insertion_sort, array4)
time_s(insertion_sort, array5)

"""
########################################################################################################
