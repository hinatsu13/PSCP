'''ISBN'''
def main():
    '''ISBN'''
    isbn = input().replace('-', '')
    ans = ((10 * int(isbn[0])) + (9 * int(isbn[1])) + (8 * int(isbn[2])) + (7 * int(isbn[3])) + \
    (6 * int(isbn[4])) + (5 * int(isbn[5])) + (4 * int(isbn[6])) + (3 * int(isbn[7])) + \
    (2 * int(isbn[8]))) * -1
    ans %= 11
    if ans == 10:
        ans = 'X'
    if str(ans) == isbn[-1]:
        print('Yes')
    else:
        print('No %s' %ans)
main()
