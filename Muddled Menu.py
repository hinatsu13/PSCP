'''Muddled Menu'''
def main():
    '''Muddled Menu'''
    menu = []
    while True:
        food = input()
        if food == 'DONE':
            break
        elif food == 'CLOSED':
            menu.clear()
            break
        elif food == "SOMETHING'S WRONG":
            menu.clear()
        elif food.count("Can't") == 1:
            food = food.replace("Can't do: ", '')
            menu.remove(food)
        else:
            dirr = food.find('#')
            num = food[dirr + 1:]
            food = food[:dirr].strip()
            if num == 'N':
                menu.insert(9999999999999, food)
            else:
                menu.insert(int(num)-1, food)
    print('Full Course:', menu, 'Reversed:', menu[::-1])
main()
