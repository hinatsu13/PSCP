'''Binary'''
def main():
    '''Binary'''
    number = int(input())
    paper = []
    while True:
        paper.append(str(number % 2))
        number = number // 2
        if number == 0:
            break
    paper.reverse()
    last = ''.join(paper)
    print(last)
main()
