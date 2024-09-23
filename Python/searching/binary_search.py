# # linear search

# def linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1


def binary_search(arr, key):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = int((l + r) / 2)
        if arr[mid] == key:
            return mid
        
        elif arr[mid] > key:
            r = mid - 1

        else:
            l = mid + 1

        return -1
    

def recursive_binary_search(arr, l, r, key):
    if l > r:
        return -1
    
    mid = int((l + r) / 2)

    if arr[mid] == key:
        return mid
    
    elif arr[mid] > key:
        return recursive_binary_search(arr, l, mid - 1, key)
    
    else:
        return recursive_binary_search(arr, mid + 1, r, key)
    


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 7))
