list = [0, 1]

def fibbanacci(index):
    first = 0
    second = 1

    if index < 2:
        return index

    for i in range(2, index+1):
        third = first + second
        first = second
        second = third

    return third

def main():
    index = int(input("Input index: "))
    element = fibbanacci(index)
    msg = f"fibanacci[{index}] it's number {element}"


main()