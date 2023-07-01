'''Harshad'''
def main():
    '''Harshad'''
    ans = 0
    paper = ''
    for _ in range(10):
        number = abs(int(input()))
        for i in range(len(str(number))):
            ans += int(str(number)[i])
        if ans == 0:
            paper += 'No\n'
        elif int(number) % ans == 0:
            paper += 'Yes\n'
        else:
            paper += 'No\n'
        ans = 0
    print(paper, end='')
main()
