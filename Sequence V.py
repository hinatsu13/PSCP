'''Sequence V'''
def main():
    '''Sequence V'''
    num = int(input())
    while True:
        for _ in range(7):
            if num == 0:
                break
            print(num, end=" ")
            num -= 1
        if num == 0:
            break
        print()
main()
