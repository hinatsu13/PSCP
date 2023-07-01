'''Shorten'''
def main():
    '''Shorten'''
    idx1 = 0
    idx2 = 0
    paper = ''
    while True:
        number = int(input())
        if number == -1:
            if paper == '':
                paper = str(idx1) if idx1 == (idx1 + idx2) \
                    else str(idx1) + '-' + str(idx1 + idx2)
            else:
                paper = paper + ', ' + str(idx1) if idx1 == (idx1 + idx2) else paper + \
                    ', ' + str(idx1) + '-' + str(idx1 + idx2)
            break
        if idx1 != number:
            if idx1 == 0:
                idx1 = number
            elif (idx1 + idx2 + 1) == number:
                idx2 += 1
            else:
                if paper == '':
                    paper = str(idx1) if idx1 == (idx1 + idx2) else str(idx1) + \
                        '-' + str(idx1 + idx2)
                else:
                    paper = paper + ', ' + str(idx1) if idx1 == (idx1 + idx2) else paper + \
                        ', ' + str(idx1) + '-' + str(idx1 + idx2)
                idx1 = number
                idx2 = 0
    print('' if paper == '0' else paper)
main()
