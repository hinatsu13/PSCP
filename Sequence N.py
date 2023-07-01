'''Sequence N'''
def main():
    '''Sequence N'''
    number = int(input())
    for row in range(number):
        for col in range(number):
            condition1 = col == 0
            condition2 = col == number - 1
            condition3 = col == row
            if condition1 or condition2 or condition3:
                print('*', end='')
            else:
                print(' ', end='')
        print()
main()
