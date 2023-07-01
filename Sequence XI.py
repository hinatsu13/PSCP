'''Sequence XI'''
def main():
    '''Sequence XI'''
    num = int(input())
    for row in range(num):
        for col in range(1, num + 1):
            if row == 0 or col - row >= 2:
                print('%02d' %(row + 1), end=' ')
            elif col == 0:
                print('%02d' %(col + 1), end=' ')
            else:
                print('%02d' %col, end=' ')
        for col in range(1, num):
            if row == 0:
                print('%02d' %(row + 1), end=' ')
            elif col == num - 1:
                print('%02d' %(1), end=' ')
            else:
                print('%02d' %(min(row + 1, abs(col - num))), end=" ")
        print()
    paper(num)

def paper(num):
    """ Sequence XI """
    for row in range(num - 1):
        for col in range(1, num + 1):
            if col == num:
                print('%02d' % (col - (row + 1)), end=' ')
            elif row == num - 2:
                print('%02d' % (row - num + 3), end=' ')
            elif col == num:
                print('%02d' % (col - (num - 1)), end=' ')
            else:
                print('%02d' % min(col, num - row - 1), end=' ')
        for col in range(1, num):
            if row == num - 2:
                print('%02d' % (row - num + 3), end=' ')
            elif col == num - 1:
                print('%02d' % (1), end=' ')
            else:
                print('%02d' % min(num - row - 1, num - col), end=' ')
        print()
main()
