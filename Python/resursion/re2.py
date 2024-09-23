# print linearly from 1 to N

n = 10

def print_n(i):
    if i > n:
        return 
    
    print(i)
    print_n(i + 1)

def main():
    print_n(1)

main()