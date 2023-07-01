'''Digit v2'''
def main():
    '''Digit v2'''
    write_num = input().split()
    if 'thousand' in write_num:
        print('4')
    elif 'hundred' in write_num:
        print('3')
    elif 'ten' in write_num or 'eleven' in write_num or 'twelve' in write_num or 'thirteen' in \
    write_num or 'fourteen' in write_num or 'fifteen' in write_num or 'sixteen' in write_num or \
    'seventeen' in write_num or 'eighteen' in write_num or 'nineteen' in write_num or \
    'twenty' in write_num or 'thirty' in write_num or 'forty' in write_num or 'fifty' in write_num \
    or 'sixty' in write_num or 'seventy' in write_num or 'eighty' in write_num or 'ninety' in \
    write_num:
        print('2')
    else:
        print('1')
main()
