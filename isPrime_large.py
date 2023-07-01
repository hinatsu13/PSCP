'''isPrime_large'''
def main():
    '''isPrime_large'''
    number = int(input())
    divide = 0
    if number == 1:
        print('NO')
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print('NO')
            return
    if divide == 0:
        print('YES')
main()
