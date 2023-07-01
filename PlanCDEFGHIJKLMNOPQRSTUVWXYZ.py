'''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
def main():
    '''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
    choice = input().lower()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if choice == 'ascend':
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        if num1 > num2:
            num1, num2 = num2, num1
        print('%.2f, %.2f, %.2f' %(num1, num2, num3))
    elif choice == 'descend':
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num3, num2 = num2, num3
        if num1 < num2:
            num1, num2 = num2, num1
        print('%.2f, %.2f, %.2f' %(num1, num2, num3))
main()
