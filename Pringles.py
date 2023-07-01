'''Pringles'''
def main():
    '''Pringles'''
    circumference = input()
    can = input()
    input()
    length = int(input())
    pringles = can.count(')')
    picked = 0
    for i in range(length):
        if can[i] == ')':
            picked += 1
    if picked == pringles:
        result = 'None.'
    else:
        result = 'There are still some left.'
    remaining = ' '*length + can[length:]
    print(picked, '\n' + result, '\n' + circumference, '\n' + remaining, '\n' + circumference)
main()
