'''Tuple's Sad life'''
def main():
    '''Tuple's Sad life'''
    number = input().split()
    want = input()
    position = number.index(want)
    for _ in range(number.count(want)):
        for _ in range(number.count(want)):
            print(position, end=' ')
        print()
main()
