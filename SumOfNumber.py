'''SumOfNumber'''
def main():
    '''SumOfNumber'''
    summ = 0
    num = int(input())
    while True:
        number = int(input())
        if number == -1:
            break
        summ += number
        if summ == num:
            break
    print(summ + (num - num))
main()
