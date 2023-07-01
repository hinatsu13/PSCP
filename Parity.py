'''Parity'''
def main():
    '''Parity'''
    number = input()
    word = input()
    ans = 0
    for i in number:
        if i == '1':
            ans += 1
    if word == 'Even':
        if ans % 2 == 0:
            print(number + '0')
        else:
            print(number + '1')
    else:
        if ans % 2 == 0:
            print(number + '1')
        else:
            print(number + '0')
main()
