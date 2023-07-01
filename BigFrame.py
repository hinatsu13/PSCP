'''BigFrame'''
def main():
    '''BigFrame'''
    word1 = input().strip()
    word2 = input().strip()
    word3 = input().strip()
    word4 = input().strip()
    word5 = input().strip()
    long = max(len(word1), len(word2), len(word3), len(word4), len(word5))
    print('*' * (long + 4))
    print('* ' + word1.ljust(long) + ' *')
    print('* ' + word2.ljust(long) + ' *')
    print('* ' + word3.ljust(long) + ' *')
    print('* ' + word4.ljust(long) + ' *')
    print('* ' + word5.ljust(long) + ' *')
    print('*' * (long + 4))
    # string method .strip()
main()
