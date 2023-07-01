'''ฉันจะเป็น Saitama ให้ได้เลย'''
import math
def main():
    '''ฉันจะเป็น Saitama ให้ได้เลย'''
    www1 = int(input()) # ต้องทำเท่าไหร่
    sss1 = int(input())
    lll1 = int(input())
    rrr1 = int(input())
    www2 = int(input()) # ได้วันละกี่ครั้ง
    sss2 = int(input())
    rrr2 = int(input())
    lll2 = int(input())
    day = www1 / www2
    if sss1 / sss2 > day:
        day = sss1 / sss2
    if lll1 / lll2 > day:
        day = lll1 / lll2
    if rrr1 / rrr2 > day:
        day = rrr1 / rrr2
    print(math.ceil(day))
main()
