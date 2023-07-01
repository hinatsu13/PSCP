'''MissingNumber'''
def main():
    '''MissingNumber'''
    num = int(input())
    paper = []
    while True:
        number = int(input())
        if number == 0:
            break
        else:
            paper.append(number)
    for i in range(1, num + 1):
        if i not in paper:
            print(i)
main()
