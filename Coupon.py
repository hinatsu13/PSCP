'''Coupon'''
def main():
    '''Coupon'''
    money = float(input())
    pro_a = list(map(float, input().split()))
    pro_b = list(map(float, input().split()))
    if money < pro_a[1] and money < pro_b[1]:
        print('Nope')
        return
    if money >= pro_a[1]:
        with_pro_a = money - pro_a[0]
    else:
        with_pro_a = 9999999
    if money >= pro_b[1]:
        with_pro_b = money * ((100 - pro_b[0]) / 100)
    else:
        with_pro_b = 9999999
    if with_pro_a < with_pro_b:
        print('1 %.1f' %with_pro_a)
    elif with_pro_b < with_pro_a:
        print('2 %.1f' %with_pro_b)
    elif with_pro_a == with_pro_b:
        if pro_a[1] < pro_b[1]:
            print('1 %.1f' %with_pro_a)
        elif pro_b[1] < pro_a[1]:
            print('2 %.1f' %with_pro_b)
        else:
            print('1 %.1f' %with_pro_a)
main()
