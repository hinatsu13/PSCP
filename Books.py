'''Books'''
import math
def main():
    '''Books'''
    books = int(input())
    pages = int(input())
    val_x = int(input())
    val_y = int(input())
    day = 0
    book = 0
    readbook = 0
    while True:
        read_day = math.ceil((val_x/val_y)*pages)
        if book == books:
            break
        if read_day >= pages:
            break
        readbook += read_day
        if readbook >= pages:
            readbook = 0
            book += 1
        val_x += 1
        val_y += 1
        day += 1
    day += (books-book)
    print(day)
main()
