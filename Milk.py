'''Milk'''
def main():
    '''Milk'''
    price = int(input())
    promotion = int(input())
    free = int(input())
    pay = int(input())
    bottles = pay // price # หาว่าซื้อได้กี่ขวด
    covers = bottles # บอกว่ามีฝากี่ฝา
    while covers >= promotion and promotion > 0: # ดูเงื่อนไขการแลกของตามโปรโมทชั่น
        change1 = (covers // promotion) * free # หาว่าแลกนมได้กี่ขวด
        change2 = covers % promotion # หาฝาที่เหลือที่ยังแลกนมไม่ได้
        bottles += change1 # ตอนนี้แลกได้แล้วกี่ขวด
        covers = change1 + change2 # เอาฝาจากขวดนมที่ได้ + ฝาขวดนมที่เหลือ
    print(bottles)
main()
