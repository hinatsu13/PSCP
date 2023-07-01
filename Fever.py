'''Fever'''
def main():
    '''Fever'''
    tem = float(input())
    if tem < 38:
        print('No Fever')
    elif tem < 39:
        print('Mild Fever')
    elif tem < 40:
        print('High Fever')
    else:
        print('Very High Fever')
main()
