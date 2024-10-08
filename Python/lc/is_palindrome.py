def isPalindrome(s):
    cls = "".join(char for char in s if char.isalnum()).lower()
    left = 0
    right = len(cls) - 1
    # print(cls)

    while left < right:
        if cls[left] != cls[right]:
            return False

        left += 1
        right -= 1

    return True


print(isPalindrome("Was it a car or a cat I saw?"))
print(sum([1, 2, 3]))
print(sorted([1, 0, 2]) == sorted([2, 1, 0]))
