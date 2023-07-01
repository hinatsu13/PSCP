'''Seeker'''
def main():
    '''Seeker'''
    password = input() + 'a'
    paper = []
    paper1 = ''
    ans = 0
    for i in password:
        if i.isdigit():
            paper1 += i
        else:
            paper.append(paper1)
            paper1 = ''
    for j in paper:
        if j == '':
            pass
        else:
            ans += int(j)
    print(ans)
main()
