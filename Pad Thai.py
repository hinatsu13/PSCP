'''Pad Thai'''
def main():
    '''Pad Thai'''
    paper_pad = []
    paper_taste = []
    pad_thai = ['Pad Thai Sauce', 'Tofu', 'Pickle Turnip', 'Shrimp', 'Bean Sprouts', 'Noodle', \
    'Chives', 'Lime', 'Egg', 'Peanuts', 'Oil']
    taste = ['Sweet', 'Sour', 'Salty']
    while True:
        pad = input()
        if pad == 'Cook':
            break
        paper_pad.append(pad)
    while True:
        tast = input()
        if tast == 'End':
            break
        paper_taste.append(tast)
    paper_pad = list(set(paper_pad))
    paper_taste = list(set(paper_taste))
    pad_thai.sort()
    taste.sort()
    paper_pad.sort()
    paper_taste.sort()
    for i in paper_pad:
        if i not in pad_thai:
            print('This is not Pad Thai!!!')
            return
    if pad_thai == paper_pad and taste == paper_taste:
        print('Delicious!')
    elif pad_thai == paper_pad and taste != paper_taste:
        print('Not Bad...')
    elif pad_thai != paper_pad:
        print('This is bad!')
main()
