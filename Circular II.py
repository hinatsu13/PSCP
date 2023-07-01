'''Circular II'''
import math
def main():
    '''Circular II'''
    me_x = float(input())
    me_y = float(input())
    redius_me = float(input())
    friend_x = float(input())
    friend_y = float(input())
    redius_friend = float(input())
    ans = math.sqrt(((me_x - friend_x) ** 2) + ((me_y - friend_y) ** 2))
    if ans < redius_me + redius_friend:
        print('Yes')
    else:
        print('No')
main()
