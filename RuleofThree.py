'''RuleofThree'''
def main():
    '''RuleofThree'''
    buy = int(input())
    paper = ''
    money1 = 0
    for i in range(buy):
        money = float(input())
        weight = float(input())
        if i == 0:
            ans = weight / money
            money1 = money
            paper = '%.2f %.2f' %(money, weight)
        if weight / money > ans:
            ans = weight / money
            money1 = money
            paper = '%.2f %.2f' %(money, weight)
        elif weight / money == ans:
            if money < money1:
                ans = weight / money
                money1 = money
                paper = '%.2f %.2f' %(money, weight)
            else:
                pass
        else:
            pass
    print(paper)
main()
