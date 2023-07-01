'''Colors'''
def main():
    '''Colors'''
    color1 = input()
    color2 = input()
    primary = ['Red', 'Blue', 'Yellow']
    if color1 not in primary or color2 not in primary:
        print('Error')
        return
    if color1 == color2:
        print(color1)
    elif (color1 == 'Red' or color1 == 'Yellow') and (color2 == 'Red' or color2 == 'Yellow'):
        print('Orange')
    elif (color1 == 'Red' or color1 == 'Blue') and (color2 == 'Red' or color2 == 'Blue'):
        print('Violet')
    elif (color1 == 'Yellow' or color1 == 'Blue') and (color2 == 'Yellow' or color2 == 'Blue'):
        print('Green')
    else:
        print('Error')
main()
