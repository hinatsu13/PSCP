'''Elo'''
def main():
    '''Elo'''
    raa = int(input())
    rbb = int(input())
    team = input().lower()
    if team == 'a':
        ans = 1 / (1 + (10 ** ((rbb - raa) / 400)))
        print('%.2f' %(round(ans, 2)))
    elif team == 'b':
        ans = 1 / (1 + (10 ** ((raa - rbb) / 400)))
        print('%.2f' %(round(ans, 2)))
main()
