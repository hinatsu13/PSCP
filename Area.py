'''Area'''
def main():
    '''Area'''
    line = int(input())
    paper = ''
    area = 0
    for _ in range(line):
        paper += input()
    for i in paper:
        if i != ' ':
            area += 1
    print(area)
main()
