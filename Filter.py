'''Filter'''
def main():
    '''Filter'''
    score = input()
    score_want = float(input())
    score = score[1:-1]
    score = score.split(', ')
    paper = []
    for i in range(len(score)):
        person = score[i].split(': ')
        if float(person[1]) >= score_want:
            paper.append(person[0][1:-1] + ' ' + person[1])
    paper.sort()
    if paper == []:
        print('Nope')
    else:
        for i in paper:
            final = i.split(' ')
            print(final[0] + '	%.2f' %(float(final[1])))
main()
