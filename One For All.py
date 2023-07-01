'''One For All'''
def main():
    '''One For All'''
    generetion = int(input())
    paper = ''
    for i in range(1, generetion + 1):
        name = input()
        if i == generetion:
            paper += name + '_' + str(generetion)
        elif i % 2 == 1:
            paper += name + '*' * i
        elif i % 2 == 0:
            paper += name + '-' * i
    print(paper)
main()
