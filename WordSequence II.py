'''WordSequence II'''
def main():
    '''WordSequence II'''
    start_word = input()
    change_word = input()
    if len(change_word) >= len(start_word):
        for i in range(len(change_word) + 1):
            print(change_word[:i] + start_word[i:])
    else:
        for i in range(len(start_word) + 1):
            if i > len(change_word):
                print(change_word + start_word[i:])
            else:
                print(change_word[:i] + start_word[i:])
main()
