'''BrickBridge'''
def main():
    '''BrickBridge'''
    small_brick = int(input())
    big_brick = int(input())
    goal = int(input())
    if (small_brick + (big_brick * 5)) < goal or goal % 5 > small_brick:
        print('-1')
    else:
        if big_brick * 5 >= goal:
            ans = goal % 5
        else:
            ans = goal - (big_brick * 5)
        print(ans)
main()
