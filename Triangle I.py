'''Triangle I'''
def main():
    '''Triangle I'''
    wood1 = float(input())
    wood2 = float(input())
    wood3 = float(input())
    if wood1 > wood2:
        wood1, wood2 = wood2, wood1
    if wood2 > wood3:
        wood2, wood3 = wood3, wood2
    woodd = (wood1 ** 2 + wood2 ** 2) ** 0.5
    if wood3 - woodd >= 0.01 or wood3 - woodd != 0:
        print('No')
    else:
        print('Yes')
main()
