'''LargestNumber'''
def main():
    '''LargestNumber'''
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    sum1 = int(str(num1) + str(num2) + str(num3))
    sum2 = int(str(num1) + str(num3) + str(num2))
    sum3 = int(str(num2) + str(num1) + str(num3))
    sum4 = int(str(num2) + str(num3) + str(num1))
    sum5 = int(str(num3) + str(num1) + str(num2))
    sum6 = int(str(num3) + str(num2) + str(num1))
    highest = 0
    if int(sum1) > highest:
        highest = sum1
    if int(sum2) > highest:
        highest = sum2
    if int(sum3) > highest:
        highest = sum3
    if int(sum4) > highest:
        highest = sum4
    if int(sum5) > highest:
        highest = sum5
    if int(sum6) > highest:
        highest = sum6
    print(highest)
main()
