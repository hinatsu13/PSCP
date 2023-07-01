'''Run Length Decoding'''
def main():
    '''Run Length Decoding'''
    sentence = input()
    paper = ''
    num = ''
    ans = ''
    for i in sentence:
        if i.isnumeric():
            num += i
        if i.isalpha():
            paper += i
            ans += int(num) * paper
            num = ''
            paper = ''
    print(ans)
main()
