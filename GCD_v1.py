'''GCD_v1'''
def main():
    '''GCD_v1'''
    num1 = int(input())
    num2 = int(input())
    paper = []
    if num1 == 0 or num2 == 0:
        print(num1 + num2)
    else:
        for i in range(1, 100001):
            if num1 % i == 0 and num2 % i == 0:
                paper.append(i)
        print(paper[-1])
main()
