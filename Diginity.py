'''Diginity'''
def main():
    '''Diginity'''
    paper = ''
    ans = 0
    while True:
        number = input()
        if number == '0':
            break
        while len(str(number)) > 1:
            for i in number:
                ans += int(i)
            number = str(ans)
            ans = 0
        paper += number + '\n'
    print(paper, end='')
main()
