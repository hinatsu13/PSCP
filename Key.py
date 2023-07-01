'''Key'''
def main():
    '''Key'''
    num = int(input())
    sum1 = 0
    for i in str(num):
        sum1 += int(i)
    sum2 = int(str(num)[-3:]) * 10
    ans = sum1 + sum2
    if ans < 1000:
        ans += 1000
    print(str(ans)[-4:])
main()
