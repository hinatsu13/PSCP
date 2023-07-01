'''Tax'''
def main():
    '''Tax'''
    year = int(input())
    ccc = int(input())
    if ccc <= 600:
        tax = ccc * 0.5
    elif ccc <= 1800:
        tax = (600 * 0.5) + ((ccc - 600) * 1.5)
    else:
        tax = (600 * 0.5) + (1200 * 1.5) + ((ccc - 1800) * 4)
    if year >= 10:
        print('%.2f' %(tax * 0.5))
    elif year >= 9:
        print('%.2f' %(tax * 0.6))
    elif year >= 8:
        print('%.2f' %(tax * 0.7))
    elif year >= 7:
        print('%.2f' %(tax * 0.8))
    elif year >= 6:
        print('%.2f' %(tax * 0.9))
    else:
        print('%.2f' %tax)
main()
