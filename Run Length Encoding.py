'''Run Length Encoding'''
def main():
    '''Run Length Encoding'''
    character = input() + ' '
    paper = ''
    ans = 1
    if len(character) == 1:
        paper = '1' + character
    for i in range(len(character) - 1):
        if character[i] == character[i + 1]:
            ans += 1
        else:
            paper += str(ans) + character[i]
            ans = 1
    print(paper)
main()
