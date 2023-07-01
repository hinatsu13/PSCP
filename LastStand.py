'''LastStand'''
def main():
    '''LastStand'''
    num = input()
    num = num[1:-1]
    num = num.split(',')
    for i in num:
        print(i[-1])
main()
