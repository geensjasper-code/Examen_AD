def isPalindroom(word):
    return isPalindromeHelper(word, 0, len(word) - 1)


def isPalindromeHelper(word, start, end):
    if end <= start:
        return True
    elif word[start] != word[end]:
        return False
    else:
        return isPalindromeHelper(word, start + 1, end - 1)

