'''GCD_v2'''
def gcd(num1, num2):
    '''find gcd'''
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

def main():
    '''GCD_v2'''
    num1 = int(input())
    num2 = int(input())
    print(gcd(num1, num2))
main()
