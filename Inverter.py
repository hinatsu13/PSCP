'''Inverter'''
def main():
    '''Inverter'''
    digital = input()
    paper = ''
    for i in range(len(digital)):
        if digital[i] == '1':
            paper += '0'
        else:
            paper += '1'
    if int(paper) == 0:
        print()
    else:
        print(int(paper))
main()
