'''Impostor'''
import json
def main():
    '''Impostor'''
    paper = {}
    die = []
    dead = {}
    countt = 0
    while True:
        character = input()
        if character == 'Start':
            break
        paper.update(json.loads(character))
    while True:
        died = input()
        if died == 'End':
            break
        die.append(died)
    for i in die:
        aaa = paper.pop(i)
        dead.update({i : aaa})
    for vlues in paper.items():
        if vlues[1] == 'Impostor':
            countt += 1
    print('%d Impostor Remains' %countt)
    print('***Alive***')
    for key, vlue in sorted(paper.items()):
        print(key, ':', vlue)
    print('***Dead***')
    for key, vlue in sorted(dead.items()):
        print(key, ':', vlue)
main()
