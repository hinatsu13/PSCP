'''RockPaperScissor'''
def main():
    '''RockPaperScissor'''
    game = input()
    player_a = 0
    player_b = 0
    for i in range(len(game)): # for i in range(0, len(game0, 2)):
        if i % 2 == 1:
            ans = game[i - 1:i + 1]
            if ans == 'RS' or ans == 'PR' or ans == 'SP':
                player_a += 1
            elif ans == 'RP' or ans == 'PS' or ans == 'SR':
                player_b += 1
        else:
            pass
    if player_a > player_b:
        print('A win %d-%d' %(player_a, player_b))
    elif player_a < player_b:
        print('B win %d-%d' %(player_b, player_a))
    elif player_a == player_b:
        print('DRAW %d' %(player_a))
main()
