# print name 5 times

name = "Archit Rathod"

# for i in range(5):
#     print(name)


def print_name(count):
    if count == 5:
        return
    print(name)
    print_name(count=count + 1)
    return


def main():
    count = 0
    print_name(count=count)


main()
