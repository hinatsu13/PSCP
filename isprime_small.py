'''isprime_small'''
def main():
    '''isprime_small'''
    number = int(input())
    divide = 0
    if number == 1:
        print('No')
        return
    for i in range(2, number + 1):
        if number % i == 0:
            divide += 1
    if divide == 1:
        print('Yes')
    else:
        print('No')
main()
