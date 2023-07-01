'''Hamburger'''
def main():
    '''hamburger meat'''
    bread_up = int(input())
    bread_down = int(input())
    print("|" * bread_up + "*" * ((bread_up + bread_down) * 2) + "|" * bread_down)
main()
