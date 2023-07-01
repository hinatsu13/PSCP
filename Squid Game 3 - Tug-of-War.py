'''Squid Game 3 - Tug-of-War'''
def main():
    '''Squid Game 3 - Tug-of-War'''
    team_a = 0
    team_b = 0
    for _ in range(10):
        force_a = int(input())
        team_a += force_a
    for _ in range(10):
        force_b = int(input())
        team_b += force_b
    if team_a < team_b:
        print('A')
    elif team_b < team_a:
        print('B')
    else:
        print('AB')
main()
