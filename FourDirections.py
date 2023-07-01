'''FourDirections'''
def roww(dirr):
    '''line 2'''
    if dirr == 'U':
        return ' ***  '
    elif dirr == 'D':
        return '  *   '
    elif dirr == 'L':
        return ' *    '
    else:
        return '   *  '

def rowww(dirr):
    '''line3'''
    if dirr == 'U' or dirr == 'D':
        return '* * * '
    else:
        return '***** '

def rowwww(dirr):
    '''line4'''
    if dirr == 'U':
        return '  *   '
    elif dirr == 'D':
        return ' ***  '
    elif dirr == 'L':
        return ' *    '
    else:
        return '   *  '

def main():
    '''FourDirections'''
    direction = input()
    paper1 = ''
    paper2 = ''
    for row in range(3):
        for dirr in direction:
            if row == 0:
                paper1 += roww(dirr)
            if row == 1:
                paper1 += rowww(dirr)
            if row == 2:
                paper1 += rowwww(dirr)
        paper2 += paper1 + '\n'
        paper1 = ''
    print('  *   ' * len(direction))
    print(paper2, end='')
    print('  *   ' * len(direction))
main()
