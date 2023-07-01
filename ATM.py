'''ATM'''
def main():
    '''ATM'''
    principle = int(input())
    while True:
        money = input()
        if money == 'END':
            break
        elif money[:2] == 'D ':
            principle += int(money[2:])
        elif money[:2] == 'W ':
            principle -= int(money[2:])
            if principle < 0:
                principle = 0
    print(principle)
main()
