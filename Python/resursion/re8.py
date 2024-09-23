#  summ of natural numbers

def sum_nos(n):
    if n == 1:
        return 1
    
    return n + sum_nos(n - 1)


print(sum_nos(10))