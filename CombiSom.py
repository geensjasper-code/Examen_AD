def combisom(lst: list[int], target: int) -> bool:
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):  # begin bij i+1 zodat je niet hetzelfde element twee keer neemt
            if lst[i] + lst[j] == target:
                return True
    return False
