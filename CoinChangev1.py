'''CoinChangev1'''
def main():
    '''CoinChangev1'''
    change = int(input())
    two_five = change // 25
    ten = (change - (two_five * 25)) // 10
    five = (change - (two_five * 25) - (ten * 10)) // 5
    one = change - (two_five * 25) - (ten * 10) - (five * 5)
    print(two_five + ten + five + one)
main()
