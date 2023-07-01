'''Kabata'''
def main():
    '''Kabata'''
    roundd = int(input())
    paper = ''
    for _ in range(roundd):
        word = input()
        while word != '':
            if word[:2] == 'ba':
                word = word[2:]
                if word[:3] == 'kka':
                    word = word[3:]
                elif word[:2] == "ka":
                    break
            elif word[:2] == "ta" or word[:2] == "ka":
                word = word[2:]
            else:
                break
        if word == '':
            paper += 'yes\n'
        else:
            paper += 'no\n'
    print(paper, end='')
main()
