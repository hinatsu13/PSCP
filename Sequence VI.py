"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()
main()
