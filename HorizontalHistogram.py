'''HorizontalHistogram'''
def checking(up_letter):
    '''low_letter'''
    paper = ''
    countt = 0
    for j in up_letter:
        countt = up_letter.count(j)
        if countt > 5:
            paper += j + ' : '
            for num in range(1, countt + 1):
                if num == countt and num % 5 == 0:
                    paper += '-'
                elif num % 5 == 0:
                    paper += '-|'
                else:
                    paper += '-'
            paper += '\n'
        elif countt != 0:
            paper += j + ' : ' + '-' * countt + '\n'
        up_letter = up_letter.replace(j, '')
        countt = 0
    return paper

def main(sentence):
    '''HorizontalHistogram'''
    word = list(sentence)
    word.sort()
    up_letter = ''
    low_letter = ''
    for i in word:
        ans = i.isupper()
        if ans == True:
            up_letter += i
        else:
            low_letter += i
    paper = ''
    countt = 0
    for k in low_letter:
        countt = low_letter.count(k)
        if countt > 5:
            paper += k + ' : '
            for num in range(1, countt + 1):
                if num == countt and num % 5 == 0:
                    paper += '-'
                elif num % 5 == 0:
                    paper += '-|'
                else:
                    paper += '-'
            paper += '\n'
        elif countt != 0:
            paper += k + ' : ' + '-' * countt + '\n'
        low_letter = low_letter.replace(k, '')
        countt = 0
    print(paper, end='')
    print(checking(up_letter), end='')
main(input())
