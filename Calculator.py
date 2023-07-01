'''Calculator'''
def main():
    '''Calculator'''
    number = int(input())
    paper = ''
    ans = 0
    if number == 1:
        print('1')
    else:
        for i in range(1, number + 1):
            paper += str(i) + '+'
        for _ in paper:
            ans += 1
        print(ans)
main()
