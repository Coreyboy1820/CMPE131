def palindrome(items):
    length = len(items)
    for i in range(length):
        if items[i] != items[length-1-i]:
            return False
    return True