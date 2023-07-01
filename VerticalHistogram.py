'''VerticalHistogram'''
def find_big(var):
    '''find capital letter'''
    if var.islower():
        return 1, var
    else:
        return 99999999, var

def main():
    '''VerticalHistogram'''
    senteace = list(input())
    senteace.sort(key=find_big)
    set_alpha = sorted(list(set(senteace)), key=find_big)
    dic_alpha = {}
    for i in set_alpha:
        dic_alpha.update({i:senteace.count(i)})
    for j in range(max(dic_alpha.values()), -1, -1):
        if j == 0:
            print('    ', end='')
        else:
            print('%03d' %j, end='')
        for k in set_alpha:
            if dic_alpha[k] >= j and j != 0:
                print(' *', end='')
            elif j == 0:
                print(k, end=' ')
            else:
                print('  ', end='')
        print()
main()
