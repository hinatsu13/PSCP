'''B - Fully pair?'''
def main():
    '''B - Fully pair?'''
    find_pair = input()
    paper = ''
    for i in find_pair:
        ans = find_pair.count(i)
        if ans % 2 == 0:
            find_pair = find_pair.replace(i, '')
        elif ans % 2 == 1:
            paper += i
            find_pair = find_pair.replace(i, '')
    if paper == '':
        print('fully paired')
    else:
        print(paper)
main()
