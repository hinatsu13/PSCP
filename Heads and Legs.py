'''Heads and Legs'''
def main():
    '''Heads and Legs'''
    heads = int(input())
    legs = int(input())
    rabbit, ghost = divmod(legs - 2 * heads, 2)
    # divmod(x//y, x%y)
    bird = heads - rabbit
    if rabbit >= 0 and bird >= 0 and ghost == 0:
        print(rabbit, bird)
    else:
        print('Impossible')
main()
