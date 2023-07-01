'''Median'''
def main():
    '''Median'''
    how_many = int(input())
    paper = []
    for _ in range(how_many):
        number = int(input())
        paper.append(number)
    paper.sort()
    if how_many % 2 == 1:
        print('%.1f' %(paper[how_many // 2]))
    else:
        ans = (int(paper[how_many // 2]) + int(paper[(how_many // 2) - 1])) / 2
        print('%.1f' %ans)
main()
