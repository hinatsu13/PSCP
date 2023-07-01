'''Coke V2'''
def main():
    '''Coke V2'''
    full_price = int(input())
    faa = int(input())
    promotion = int(input())
    want = int(input())
    if want == 0:
        print('0')
        return
    if faa == 0:
        print(want * full_price)
        return
    price_pro = ((faa - 1) * full_price) + promotion
    bottle_pro = (want - 1) // faa
    not_in = ((want - 1) % faa) * full_price
    print((price_pro * bottle_pro) + not_in + full_price)
main()
