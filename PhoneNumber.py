'''PhoneNumber'''
def main():
    '''PhoneNumber'''
    tell = input()
    country = input()
    if country == "Domestic":
        if len(tell) == 9:
            print(tell[0] + ' ' + tell[1:5] + ' ' + tell[5:])
        else:
            print(tell[:2] + ' ' + tell[2:6] + ' ' + tell[6:])
    elif country == "International":
        if len(tell) == 10:
            print('+66' + tell[1], tell[2:6], tell[6:])
        else:
            print('+66 ' + tell[1:5] + ' ' + tell[5:])
main()
