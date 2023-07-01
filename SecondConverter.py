'''SecondConverter'''
def main():
    '''SecondConverter'''
    kkk = int(input()) #วินาทีโลก
    sss = int(input()) #คู่ขนานจะมีระยะเวลา s วินาที
    mmm = int(input()) #คู่ขนานชั่วโมงจะมีเวลา m นาที
    hhh = int(input()) #คู่ขนานหนึ่งวันมี h ชั่วโมง
    minutes = kkk // sss
    hours = minutes // mmm
    kkk = kkk % sss
    minutes = minutes % mmm
    hours = hours % hhh
    print('%d:%d:%d' %(hours, minutes, kkk))
main()
