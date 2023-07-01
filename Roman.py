'''Roman'''
def main():
    '''Roman'''
    rom = input()
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, \
    'XL':40, 'XC':90, 'CD':400, 'CM':900}
    roundd = 0
    num = 0
    while roundd < len(rom):
        if roundd + 1 < len(rom) and rom[roundd:roundd + 2] in roman:
            num += roman[rom[roundd:roundd + 2]]
            roundd += 2
        else:
            num += roman[rom[roundd]]
            roundd += 1
    print(num)
main()
