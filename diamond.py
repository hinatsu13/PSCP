'''diamond'''
def main():
    '''diamond'''
    num = int(input())
    for row in range(num // 2):
        for col in range(num):
            if row + col == num // 2:
                print('*', end=' ')
            elif col - row == num // 2 - 1 and col >= num // 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print('*' * num)
    for row in range(num // 2):
        for col in range(num):
            if col - row == 1:
                print('*', end='')
            elif row + col == num - 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()
main()
