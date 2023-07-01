'''Restaurant'''
def main():
    '''Restaurant'''
    bill = float(input())
    promotion = float(input())
    discount = float(input())
    offer = float(input())
    if bill + offer >= promotion:
        with_pro = (bill + offer) * (100 - discount) / 100
    else:
        with_pro = bill + offer
    if bill >= promotion:
        without_pro = bill * (100 - discount) / 100
    else:
        without_pro = bill
    ans = abs(with_pro - without_pro)
    if without_pro > with_pro:
        print('Yes %.3f' %ans)
    elif with_pro > without_pro:
        print('No %.3f' %ans)
    else:
        print('Yes')
main()
