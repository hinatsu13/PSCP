'''Parallelogram'''
def main():
    '''Parallelogram'''
    word = input()
    for i in range(len(word)):
        print(' ' * (len(word) - i - 1) + word[:i + 1])
    for i in range(len(word) - 1):
        print(word[i + 1:])
main()
