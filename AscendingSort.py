'''AscendingSort'''
def main():
    '''AscendingSort'''
    paper = []
    for _ in range(5):
        num = int(input())
        paper.append(num)
    paper.sort()
    for i in paper:
        print(i)
main()
