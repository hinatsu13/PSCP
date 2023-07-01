'''SurprisingVote'''
def main():
    '''SurprisingVote'''
    summ = float(input()) # total score
    highest = float(input()) # highest score
    ans = 0
    if highest == 2:
        print('Not surprising')
        return
    if highest * 2 < summ:
        ans += summ - highest
    if abs(ans - highest * 2) > 2:
        print('Surprising')
    else:
        print('Not surprising')
main()
