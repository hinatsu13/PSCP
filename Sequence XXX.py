'''SequenceXXX'''
def main():
    '''SequenceXXX'''
    size = int(input())
    xbox = int(input())
    paper1 = ''
    paper2 = ''
    for row in range(size):
        for col in range(size):
            if col == row or col == 0 or row == 0 or row == size - 1 \
            or col == row - (size - 1) or row == size - (col + 1) or col == size - 1:
                paper1 += '*'
            else:
                paper1 += ' '
        paper2 += (paper1 + ' ') * xbox + '\n'
        paper1 = ''
    print(paper2, end='')
main()
