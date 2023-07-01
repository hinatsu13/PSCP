'''Backward'''
def main():
    '''Backward'''
    paper = []
    while True:
        word = input()
        if word == 'NULL':
            break
        else:
            paper.append(word)
    paper.reverse()
    for i in paper:
        print(i)
main()
