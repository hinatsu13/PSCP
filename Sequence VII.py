'''Sequence VII'''
def main():
    '''Sequence VII'''
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()

    for row in range(num, 1, -1):
        for col in range(row):
            if col == 0:
                pass
            else:
                print(col, end=" ")
        print()
main()
