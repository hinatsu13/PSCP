'''PickThem'''
def main():
    '''PickThem'''
    num = input()
    num = num[1:-1]
    lisst = num.split(', ')
    roundd = 0
    paper = ''
    for i in lisst:
        if int(i) % 2 == 0:
            roundd += 1
            paper += i + '\n'
        else:
            pass
    if roundd == 0:
        print('Nope')
    else:
        print(paper, end='')
main()
