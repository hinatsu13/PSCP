'''Diamond I'''
def main():
    '''Diamond I'''
    row = int(input())
    col = int(input())
    paper = []
    for i in range(row):
        diamond = [int(x) for x in input().split()]
        if i == 0:
            paper = diamond
        else:
            for j in range(col):
                paper[j] = int(paper[j]) + int(diamond[j])
    print(max(paper))
main()
