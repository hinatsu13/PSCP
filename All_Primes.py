'''All_Primes'''
def main():
    '''All_Primes'''
    range_number = int(input())
    divide = 0
    prime = 0
    for i in range(1, range_number + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                divide += 1
        if divide == 2:
            prime += 1
        divide = 0
    print(prime)
main()
