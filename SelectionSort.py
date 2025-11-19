def selection_sort(data):
    """
    Sorts a list of elements using the Selection Sort algorithm.

    Args:
        data (list): The list of elements to be sorted.
    """
    n = len(data)

    # Traverse through all elements in the list
    for i in range(n):
        # Assume the current position 'i' holds the minimum value
        min_idx = i

        # Inner loop: Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            # If a smaller element is found, update min_idx
            if data[j] < data[min_idx]:
                min_idx = j

        # After the inner loop, min_idx holds the index of the minimum element
        # Swap the found minimum element with the element at the current position 'i'
        data[i], data[min_idx] = data[min_idx], data[i]

    # The list 'data' is now sorted in place
    return data

# --- Example Usage ---

unsorted_list = [64, 25, 12, 22, 11]
print(f"Original list: {unsorted_list}")

sorted_list = selection_sort(unsorted_list)
print(f"Sorted list: {sorted_list}")

# Another example
list_b = [5, 1, 4, 2, 8]
selection_sort(list_b)
print(f"Sorted list B: {list_b}")