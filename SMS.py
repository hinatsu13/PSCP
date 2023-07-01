'''SMS'''
def main():
    '''SMS'''
    botton = int(input())
    character = {2:['A', 'B', 'C'], 3:['D', 'E', 'F'], 4:['G', 'H', 'I'], 5:['J', 'K', 'L'], \
    6:['M', 'N', 'O'], 7:['P', 'Q', 'R', 'S'], 8:['T', 'U', 'V'], 9:['W', 'X', 'Y', 'Z']}
    paper = ''
    for _ in range(botton):
        num = int(input())
        push = int(input())
        if num == 1:
            for _ in range(push):
                paper = paper[:len(paper) - 1]
        elif push != 0:
            push = push % len(character[num]) - 1
            paper += character[num][push]
    if paper == '':
        print('null')
    else:
        print(paper)
main()
