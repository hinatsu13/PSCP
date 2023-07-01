'''3nPlus1'''
def main():
    '''3nPlus1'''
    paper = ''
    countt = 1
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            while True:
                if num == 1:
                    paper += str(countt) + '\n'
                    countt = 1
                    break
                elif num % 2 == 0:
                    num = num / 2
                    countt += 1
                else:
                    num = (num * 3) + 1
                    countt += 1
    print(paper, end='')
main()
