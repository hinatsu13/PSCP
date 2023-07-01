'''Volleyball'''
def check(win_a, win_b, sett, score_a, score_b):
    '''who win'''
    if win_a > win_b and win_a == 3:
        print('A won %d:%d set' %(win_a, win_b))
    elif win_b > win_a and win_b == 3:
        print('B won %d:%d set' %(win_b, win_a))
    else:
        print('Set %d: A (%d) | B (%d)\nThe game has not finished yet.' \
        %(sett, score_a, score_b))

def main():
    '''Volleyball'''
    volley = input()
    score_a = 0
    score_b = 0
    sett = 1
    win_a = 0
    win_b = 0
    for i in volley:
        if i == 'A':
            score_a += 1
        elif i == 'B':
            score_b += 1

        if sett == 5:
            if (score_a > 14 or score_b > 14) and abs(score_a - score_b) >= 2:
                print('Set 5: A (%d) | B (%d)' %(score_a, score_b))
                if score_a > score_b:
                    win_a += 1
                else:
                    win_b += 1
        elif (score_a > 24 or score_b > 24) and abs(score_a - score_b) >= 2:
            print('Set %d: A (%d) | B (%d)' %(sett, score_a, score_b))
            if score_a > score_b:
                win_a += 1
            else:
                win_b += 1
            score_a = 0
            score_b = 0
            sett += 1
    check(win_a, win_b, sett, score_a, score_b)
main()
