'''Sequence III'''
def main():
    '''Sequence III'''
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            col += row
            print(col, end=' ')
        print()
main()
