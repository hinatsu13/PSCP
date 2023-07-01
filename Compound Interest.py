'''Compound Interest'''
def main():
    '''Compound Interest'''
    money, rate, time = int(input()), float(input()), int(input())
    for _ in range(time):
        money = money * (100 + rate) / 100
    print('%.2f' % money)
main()
