'''Align'''
def main():
    '''Align'''
    num = int(input())
    position = input().lower()
    word = input()
    if position == 'left':
        print(word.ljust(num))
    elif position == 'right':
        print(word.rjust(num))
    elif position == 'center':
        word2 = word.center(num)
        space = word2.count(" ")
        if space % 2 == 1:
            print(" "*int((space+1)/2), end="")
            print(word, end="")
            print(" "*int((space-1)/2), end="")
        else:
            print(word2)
main()
