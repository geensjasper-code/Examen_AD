def binary_search(data, target):
    """
    Performs binary search on a sorted list to find the target value.

    Args:
        data (list): The sorted list of elements to search through.
        target: The value to search for.

    Returns:
        int: The index of the target in the list, or -1 if the target is not found.
    """
    low = 0
    high = len(data) - 1

    # Keep searching while the search range is valid
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        # Get the value at the middle index
        guess = data[mid]

        # Check if the target is found
        if guess == target:
            return mid # Target found, return its index

        # If the guess is too high, ignore the right half (including the middle)
        elif guess > target:
            high = mid - 1

        # If the guess is too low, ignore the left half (including the middle)
        else:
            low = mid + 1

    # If the loop finishes without finding the target, it means the target is not in the list
    return -1

# --- Example Usage ---

sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
search_target = 23

# Search for 23
index = binary_search(sorted_list, search_target)

if index != -1:
    print(f"Target {search_target} found at index: {index}")
else:
    print(f"Target {search_target} not found in the list.")

# Search for a value not in the list (e.g., 42)
search_target_missing = 42
index_missing = binary_search(sorted_list, search_target_missing)

if index_missing != -1:
    print(f"Target {search_target_missing} found at index: {index_missing}")
else:
    print(f"Target {search_target_missing} not found in the list.")