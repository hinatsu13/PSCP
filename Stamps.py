'''Stamps'''
def main():
    '''Stamps'''
    count = int(input())
    pay_promotion = int(input())
    free_stamp = int(input())
    stamp_discount = int(input())
    discount = int(input())
    total = 0
    stamp = 0
    for _ in range(count):
        bill = int(input())
        while bill > 0 and stamp >= stamp_discount:
            stamp -= stamp_discount
            bill = max(bill - discount, 0)
        total += bill
        stamp += free_stamp * (bill // pay_promotion)
    print(str(total) + '\n' + str(stamp))
main()
