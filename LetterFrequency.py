'''LetterFrequency'''
def main():
    '''LetterFrequency'''
    letter = input().lower().replace(' ', '')
    highest = 0
    countt = 0
    ans = ''
    for i in letter:
        countt = letter.count(i)
        if countt > highest:
            ans = i
            highest = countt
        countt = 0
        letter = letter.replace(i, '')
    print(ans)
main()
