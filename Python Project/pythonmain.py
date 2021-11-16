"""
********************************************************************************************************************************************************************************
Function Name: - bubbleSort
********************************************************************************************************************************************************************************
Description  : - Sorts in array in ascending order by comparing every integer to every other integer in the array and doing that n times till the array is sorted
               - By Nature moves the highest number to the end of the array, then starts over
Input        : - Takes in an unsorted array as input
Ouput        : - Returns a sorted array 
********************************************************************************************************************************************************************************
"""


def bubbleSort(Array):

    new_array = []
    Array = flatten(Array, new_array)
    Array = removeNone(Array)

    if numOfElements(Array) == True:
        return "Array contains 10000 elements, can not be processed"
    else:
        for i in range(len(Array) - 1):
            for j in range(0, len(Array) - i - 1):
                if Array[j] > Array[j + 1]:
                    temp = Array[j]
                    Array[j] = Array[j + 1]
                    Array[j + 1] = temp

        return Array


"""
********************************************************************************************************************************************************************************
Function Name: - flatten
********************************************************************************************************************************************************************************
Description  : - Takes a multi-dimensional array (could be more greater than a 2-D array i.e Nested arrays within Nested arrays and converts it into a single array (1-D array)
               - Makes use of recursion to access nested arrays within nested arrays
Input        : - Takes in a nested array + an empty array
Ouput        : - Returns a single 1-D array
********************************************************************************************************************************************************************************
"""


def flatten(arr, newarr):
    i = 0
    while i < len(arr):
        if isinstance(arr[i], list) == True:
            recursive_call = flatten(arr[i], newarr)
        else:
            newarr.append(arr[i])

        i = i + 1

    return newarr


"""
********************************************************************************************************************************************************************************
Function Name: - removeNone
********************************************************************************************************************************************************************************
Description  : - Removes Null values from the array
Input        : - Takes in a 1-D array i.e after being flattened
Ouput        : - Returns an array containing only integers
********************************************************************************************************************************************************************************
"""


def removeNone(arr):
    int_array = []

    for i in arr:
        if i != None:
            int_array.append(i)
    return int_array


"""
********************************************************************************************************************************************************************************
Function Name: - numOfElements
********************************************************************************************************************************************************************************
Description  : - Returns the number of elements in the array
Input        : - Takes in a flatten array
Ouput        : - Returns the number of elements in the array
********************************************************************************************************************************************************************************
"""


def numOfElements(array):
    if len(array) > 10000:
        return True
    else:
        return False


"""
********************************************************************************************************************************************************************************
-- MAIN
********************************************************************************************************************************************************************************
"""

if __name__ == "__main__":
    arr = [6, 2, [4, 3], [[[5], None], 1]]
    arr = bubbleSort(arr)
    print(arr)

    arr2 = [5,4,3,2,1]
    arr2 = bubbleSort(arr2)
    print(arr2)
