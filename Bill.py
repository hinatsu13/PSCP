'''Bill'''
def main():
    '''Bill'''
    price = float(input())
    service = price * (10 / 100)
    if service < 50:
        price += 50
    elif service > 1000:
        price += 1000
    else:
        price += service
    vat = price + (price * (7 / 100))
    print('%.2f' %(round(vat, 2)))
main()
