'''ValidVar'''
def main():
    '''ValidVar'''
    num = int(input())
    paper = ''
    for _ in range(num):
        name = input()
        if not name.strip().isidentifier(): # หาอักขระพิเศษ
            paper += 'Invalid\n'
        elif name[0] == '0' or name[0] == '1' or name[0] == '2' or name[0] == '3' or \
                name[0] == '4' or name[0] == '5' or name[0] == '6' or name[0] == '7' or \
                name[0] == '8' or name[0] == '9':
            paper += 'Invalid\n'
        elif ' ' in name:
            paper += 'Invalid\n'
        elif name == 'if' or name == 'else' or name == 'elif' or name == 'while' or \
                name == 'for' or name == 'True' or name == 'False' or name == 'continue' or \
                name == 'break' or name == 'return' or name == 'is' or name == 'in' or \
                name == 'and' or name == 'or' or name == 'from' or name == 'as' or \
                name == 'pass' or name == 'not' or name == 'def' or name == 'None':
            paper += 'Invalid\n'
        else:
            paper += 'Valid\n'
    print(paper, end='')
main()
