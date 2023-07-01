'''Sequence IX'''
def main():
    '''Sequence IX'''
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, (num + 1) - row):
            print("   ", end="")
        for col in range(1, row + 1):
            print('%02d' %col, end=" ")
        for col in range(2, row + 1):
            print('%02d' %(row - col + 1), end=" ")
        print()
main()
