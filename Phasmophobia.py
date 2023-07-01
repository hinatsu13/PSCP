'''Phasmophobia'''
def findd(ghost, many_evi):
    '''find ghost'''
    ans = ''
    for i in range(len(ghost)):
        if ghost[i] == ghost[i - 1]:
            pass
        elif ghost.count(ghost[i]) == many_evi:
            ans += ghost[i] + '\n'
    if ans == '':
        return 'Not yet discovered'
    else:
        return ans

def main():
    '''Phasmophobia'''
    paper = ''
    many_evi = 3
    for _ in range(3):
        evidence = input()
        if evidence == 'EMF Level 5':
            paper += ' Banshee Jinn Oni Phantom Revenant Shade'
        elif evidence == 'Ghost Writing':
            paper += ' Demon Oni Revenant Shade Spirit Yurei'
        elif evidence == 'Fingerprints':
            paper += ' Banshee Poltergeist Revenant Spirit Wraith'
        elif evidence == 'Spirit Box':
            paper += ' Demon Jinn Mare Oni Poltergeist Spirit Wraith'
        elif evidence == 'Freezing Temperatures':
            paper += ' Banshee Demon Mare Phantom Wraith Yurei'
        elif evidence == 'Ghost Orb':
            paper += ' Jinn Mare Phantom Poltergeist Shade Yurei'
        else:
            many_evi -= 1
    paper = paper.split()
    paper.sort()
    if many_evi == 0:
        print('Banshee\nDemon\nJinn\nMare\nOni\nPhantom\nPoltergeist\nRevenant\nShade\nSpirit \
        \nWraith\nYurei')
        return
    else:
        print(findd(paper, many_evi), end='')
main()
