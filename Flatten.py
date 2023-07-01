'''Flatten'''
import json
def main():
    '''Flatten'''
    list_want = input()
    list_want = json.loads(list_want)
    paper = []
    while True:
        if len(list_want) == 0:
            break
        temp = []
        for i in range(len(list_want)):
            if isinstance(list_want[i], (int, float)):
                paper.append(list_want[i])
            else:
                for j in list_want[i]:
                    temp.append(j)
        list_want = temp
    print(sorted(paper)[::-1])
main()
