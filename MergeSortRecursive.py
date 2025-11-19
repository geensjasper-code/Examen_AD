def mergesort(lijst):
    if len(lijst) <= 1:
        return lijst

    mid = len(lijst) // 2
    deel1 = mergesort(lijst[:mid])
    deel2 = mergesort(lijst[mid:])

    return merge(deel1, deel2)


def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


# Test
mergesort([3, 3, 4, 8, 5, 2, 7])