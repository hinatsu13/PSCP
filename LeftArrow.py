'''LeftArrow'''
def main():
    '''light'''
    colum = int(input())
    rows = int(input())
    for i in range((rows // 2), rows - 1):
        for _ in range(0, rows-i-1):
            print(" ", end="")
        for _ in range(0, colum):
            print("*", end="")
        print()
    for i in range(0, rows - (rows // 2)):
        for _ in range(1, i+1):
            print(" ", end="")
        for _ in range(0, colum):
            print("*", end="")
        print()
main()
