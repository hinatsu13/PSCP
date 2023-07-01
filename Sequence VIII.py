'''Sequence VIII'''
def main():
    '''Sequence VIII'''
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, num + 1 - row):
            print('   ', end='')
        for col in range(1, row + 1):
            print('%02d' %col, end=' ')
        print()
main()
