'''Point Sorting'''
def main():
    '''Point Sorting'''
    testing = int(input())
    paper = []
    ans = ''
    for _ in range(testing):
        test_case = int(input())
        for _ in range(test_case):
            case = [int(x) for x in input().split()]
            paper.append(case)
        summ = sorted(paper, key=lambda i: (sum(i), -i[1]))
        for i in summ:
            answer = [str(y) for y in i]
            ans += ' '.join(answer) +'\n'
        paper = []
    print(ans, end='')
main()
