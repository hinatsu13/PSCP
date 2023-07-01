'''LineSorting'''
def main():
    '''LineSorting'''
    roundd = int(input())
    paper = []
    for _ in range(roundd):
        word = input()
        paper.append(word)
    paper.sort(key=len)
    for i in paper:
        print(i)
main()
