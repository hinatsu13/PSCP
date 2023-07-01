'''PickThemAgain'''
def main():
    '''PickThemAgain'''
    num = input()
    listt = num.split(' ')
    listt.reverse()
    roundd = 0
    paper = ''
    for i in listt:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            roundd += 1
            paper += i + '\n'
        else:
            pass
    if roundd == 0:
        print('Nope')
    else:
        print(paper, end='')
main()
