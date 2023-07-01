'''Nearer'''
def main():
    '''Nearer'''
    alice = int(input())
    bob = int(input())
    car = int(input())
    distance_alice = abs(car - alice)
    distance_bob = abs(car - bob)
    if distance_alice < distance_bob:
        print('Alice %d' %distance_alice)
    elif distance_bob < distance_alice:
        print('Bob %d' %distance_bob)
    else:
        print('Sundaes %d' %distance_bob)
main()
