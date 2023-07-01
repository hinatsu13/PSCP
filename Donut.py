'''Donut'''
def main():
    '''Donut'''
    price = int(input())
    promo = int(input())
    free = int(input())
    want = int(input())
    purchase = want // (promo + free) # ดูว่าได้โปรโมชั่นกี่ครั้ง
    donut = (want // (promo + free)) * (promo + free) # ได้โดนัทกี่ชิ้น
    pay = price * promo * purchase # คิดราคาโดนัทที่ซื้อ
    # ดูเงื่อนไขอื่นๆที่เป็นไปได้
    if want % (promo + free) >= promo:
        donut += promo + free
        pay += price * promo
    else:
        buy = want - donut
        donut += buy
        pay += price * buy
    print('%d %d' %(pay, donut))
main()
