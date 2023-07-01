'''GCD_N'''
def gcd(num1, num2):
    '''find gcd'''
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def main():
    '''GCD_N'''
    roundd = int(input())
    paper = []
    for _ in range(roundd):
        paper.append(int(input()))
    if roundd == 1:
        print(*paper)
        return
    num1 = paper[0]
    num2 = paper[1]
    num = gcd(num1, num2)
    for i in range(2, len(paper) - 1):
        num = gcd(num, paper[i])
    print(num)
main()
    