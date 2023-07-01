'''MAC'''
def valid_1(checkk):
    '''chack 1'''
    ans = 0
    for i in range(len(checkk)):
        if len(checkk[i]) == 2:
            ans += 1
    if ans == 6:
        return 'VALID 1'
    else:
        return 'ERROR'

def valid_2(checkk):
    '''chack 1'''
    ans = 0
    for i in range(len(checkk)):
        if len(checkk[i]) == 2:
            ans += 1
    if ans == 6:
        return 'VALID 2'
    else:
        return 'ERROR'

def valid_3(checkk):
    '''chack 1'''
    ans = 0
    for i in range(len(checkk)):
        if len(checkk[i]) == 4:
            ans += 1
    if ans == 3:
        return 'VALID 3'
    else:
        return 'ERROR'

def main():
    '''MAC'''
    address, check = input(), 0
    for i in address:
        if i not in "0123456789ABCDEF.-:" and i not in "0123456789abcdef.-:" or\
           (i == "-" and address.count(i) > 5) or (i == ":" and address.count(i) > 5) or\
           (i == "." and address.count(i) > 2):
            check = 1
            break
    if '-' in address and check == 0:
        checkk = address.split('-')
        print(valid_1(checkk))
    elif ':' in address and check == 0:
        checkk = address.split(':')
        print(valid_2(checkk))
    elif '.' in address and check == 0:
        checkk = address.split('.')
        print(valid_3(checkk))
    else:
        print('ERROR')
main()
