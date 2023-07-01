'''Century'''
def main():
    '''Century'''
    num = int(input())
    paper = ''
    for _ in range(num):
        year = input()
        year_num = year[5:]
        if year[:5] == 'B.E. ' and int(year_num) > 543:
            if str(int(year_num) - 543)[-2:] == '00':
                paper += str((int(year_num) - 543) // 100) + '\n'
            else:
                paper += str((int(year_num) - 543) // 100 + 1) + '\n'
        elif year[:5] == 'A.D. ' and int(year_num) > 0:
            if year[-2:] == '00':
                paper += str(int(year_num) // 100) + '\n'
            else:
                paper += str(int(year_num) // 100 + 1) + '\n'
        else:
            paper += 'ERROR\n'
    print(paper, end='')
main()
