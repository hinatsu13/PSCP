'''Sequence XII'''
def main():
    '''Sequence XII'''
    num = int(input())
    for row in range(-num + 1, num):
        for col in range(-num + 1, num):
            print('%02d' %(num - abs(abs(row) - abs(col))), end=' ')
        print()
main()
