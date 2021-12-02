"""Sorting algorithms for lists that contain integer values."""

from typing import List

from random import randint

# Reference for some algorithm implementations:
# https://realpython.com/sorting-algorithms-python/

# TODO: Add all of the source code based on the above article


def bubble_sort(array: List[int]) -> List[int]:
    """Sort an input list called array using bubble sort."""
    num = len(array)

    for i in range(num):
        # Create a flag for when there's nothing left to sort
        already_sorted = True

        # Start looking at the list if it has already been sorted
        for j in range(num - i - 1):
            if array[j] > array[j + 1]:
                # If it is greater than, then swap it
                array[j], array[j + 1] = array[j + 1], array[j]
                # Wasn't sorted, so set flag to false
                already_sorted = False

        # With no swaps, terminate for loop
        if already_sorted:
            break
    return array


def insertion_sort(array: List[int]) -> List[int]:
    """Run an insertion sort on the provided array."""
    # Loop from the second element to the last element
    for i in range(1, len(array)):
        # Pick element to position
        key_item = array[i]
        # Initializes the varible to find correct postition in list
        j = i - 1
        # Run through the list and find right position for key_item
        # ONLY if key_item is smaller than adjacent values
        while j >= 0 and array[j] > key_item:
            # shift the position to move j
            array[j + 1] = array[j]
            j -= 1
        # After finish shifting the elements, put key_item into correct location
        array[j + 1] = key_item
    return array


def merge(left: List[int], right: List[int]) -> List[int]:
    """Define a convenience method that supports the merging of lists."""
    # Check for empty arrays
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Iterate through both arrays until all elements are in the combined array
    while len(result) < len(left) + len(right):
        # Sort into resultant array, grab from left and right array in order
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If reach the end of an array, add the rest of one array and break
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array: List[int]) -> List[int]:
    """Sort the provided list called array with the merge sort algorithm."""
    # If array has less than 2 elements, return it as result
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort array through recursively spitting into halves
    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


def quick_sort(array: List[int]) -> List[int]:
    """Sort the provided list called array with the quick sort algorithm."""
    # If array is less than 2 elements, return it as the result
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Look if elements are smaller than pivot
        if item < pivot:
            # Add to low list
            low.append(item)
        # Is same value as pivot
        elif item == pivot:
            # Add to same list
            same.append(item)
        # Is larger value than pivot
        elif item > pivot:
            # Add to high list
            high.append(item)
    # Final result combines all the lists
    return quick_sort(low) + same + quick_sort(high)


def insertion_sort_tim(array: List[int], left: int = 0, right=None):
    """Use an internal sorting algorithm for the timsort algorithm."""
    if right is None:
        right = len(array) - 1

    # Look through array from left item to right item
    for i in range(left + 1, right + 1):
        # Position item in correct location
        key_item = array[i]

        # Initialize variable to find correct position of the key_item
        j = i - 1

        # Run through the list of items (the left side), find correct position
        # ONLY if key_item is smaller than adjacent
        while j >= left and array[j] > key_item:
            # Shift value a position to the left and move j to next point
            array[j + 1] = array[j]
            j -= 1

        # When done shifting elements, move key_item to correct location
        array[j + 1] = key_item

    return array


def tim_sort(array: List[int]) -> List[int]:
    """Sort the list called array with the tim sort algorithm using a special insertion sort."""
    min_run = 32
    num = len(array)

    # Start slicing and sorting small sections
    for i in range(0, num, min_run):
        insertion_sort_tim(array, i, min((i + min_run - 1), num - 1))

    # Merge sorted slices starting form min_run and doubling size on each iteration
    size = min_run
    while size < num:
        # Determine arrays the will be merged together
        for start in range(0, num, size * 2):
            # Compute midpoint(first array ends and second starts) and endpoint(second array ends)
            midpoint = start + size - 1
            endpoint = min((start + size * 2 - 1), (num - 1))

            # Merge the two subarrays
            mergedArray = merge(
                left=array[start : midpoint + 1],
                right=array[midpoint + 1 : endpoint + 1],
            )

            # Put merged array as array
            array[start : start + len(mergedArray)] = mergedArray

        # Each iteration doubles the size of arrays
        size *= 2

    return array
