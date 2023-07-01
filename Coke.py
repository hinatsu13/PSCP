'''Coke'''
def main():
    '''Coke'''
    price = int(input())
    cap = int(input())
    lowprice = int(input())
    bottle_want = int(input())
    pay = 0
    bottle = 0
    countt = 0
    new_price = price
    while countt < bottle_want:
        bottle += 1
        countt += 1
        pay += new_price
        new_price = price
        if bottle == cap:
            bottle = 0
            new_price = lowprice
    print(pay)
main()
