'''BookWorm'''
def main():
    '''BookWorm'''
    testing = int(input())
    paper = []
    countt = 0
    ans = 0
    paper1 = ''
    for _ in range(testing):
        timing = int(input())
        book = int(input())
        for _ in range(book):
            read = int(input())
            paper.append(read)
        paper.sort()
        for i in paper:
            if i + countt <= timing:
                ans += 1
                countt += i
        paper1 += str(ans) + '\n'
        ans = 0
        countt = 0
        paper = []
    print(paper1, end='')
main()
