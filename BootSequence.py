'''BootSequence'''
def main():
    '''BootSequence'''
    num = int(input())
    paper = ''
    for i in range(1, num + 1):
        if i != num:
            paper = paper + str(i) + '_'
        else:
            paper = paper + str(i)
    print(paper)
    # for i in range(1, num + 1):
    #     print(i, end=' ', sep='_')
main()
