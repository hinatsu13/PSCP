'''Matrix_MN'''
def main():
    '''Matrix_MN'''
    row = int(input())
    col = int(input())
    paper = ''
    for _ in range(row):
        for _ in range(col):
            num = input()
            paper += num +' '
        paper += '\n'
    print(paper, end='')
main()
