'''HowLong'''
def main():
    '''HowLong'''
    number = input()
    summ = 0
    for _ in number:
        summ += 1
    if '-' in number:
        summ = summ - 1
    print(summ)
main()
