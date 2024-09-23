# power of a number - a ^ b
def power(a, b):
    if b == 0:
        return 1
    
    return a * power(a, b - 1)

print(power(5, 3))