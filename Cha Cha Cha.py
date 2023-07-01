'''Cha Cha Cha'''
import math
def main():
    '''Cha Cha Cha'''
    day = int(input())
    money = 0
    for _ in range(day):
        hours = float(input())
        money += 8720 * (math.ceil(hours))
    print(int(money))
main()
