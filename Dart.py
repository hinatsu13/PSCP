'''Dart'''
def main():
    '''Dart'''
    num = int(input())
    score = 0
    for _ in range(num):
        position = [int(x) for x in input().split()]
        where = ((position[0] ** 2) + (position[1] ** 2)) ** 0.5
        if where <= 2:
            score += 5
        elif where <= 4:
            score += 4
        elif where <= 6:
            score += 3
        elif where <= 8:
            score += 2
        elif where <= 10:
            score += 1
    print(score)
main()
