'''OneTwo'''
def main():
    '''OneTwo'''
    num = int(input())
    paper = ['0']
    for i in range(1, num + 1):
        if i == 1:
            paper.append('1')
        elif i == 2:
            paper.append('2')
        else:
            paper.append(paper[i-1] + paper[i-2])
    print(paper[-1])
main()
