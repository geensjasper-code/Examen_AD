def sort(lijst):
    """
    Sorteer de lijst 'lijst' in-place met QuickSort.
    """

    def quicksort_inplace(arr, low, high):
        if low < high:
            # Partitioneer de lijst en krijg de index van de pivot
            pivot_index = partition(arr, low, high)
            # Recursief sorteer links van pivot
            quicksort_inplace(arr, low, pivot_index - 1)
            # Recursief sorteer rechts van pivot
            quicksort_inplace(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]  # kies laatste element als pivot
        i = low - 1  # index van het laatste element kleiner dan pivot

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # swap
        # plaats pivot op juiste plek
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort_inplace(lijst, 0, len(lijst) - 1)