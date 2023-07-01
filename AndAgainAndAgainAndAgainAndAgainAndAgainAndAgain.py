'''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
def main():
    '''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
    sentence = input().replace('.', '').split()
    paper = []
    countt = 0
    for i in sentence:
        for j in i:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                countt += 1
        if countt >= 2:
            paper.append(i)
        countt = 0
    if paper == []:
        print('Nope')
    else:
        paper.sort()
        for j in paper:
            print(j)
main()
