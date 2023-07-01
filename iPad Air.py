'''iPad Air'''
def main():
    '''iPad Air'''
    color = input()
    memory = input()
    connecting = input()
    ipad_color = ['Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue']
    if color not in ipad_color:
        print('Not Available')
        return
    if memory == '64' and connecting == 'Wi-Fi':
        print('19900')
    elif memory == '256' and connecting == 'Wi-Fi':
        print('24900')
    elif memory == '64' and connecting == 'Wi-Fi + Cellular':
        print('24400')
    elif memory == '256' and connecting == 'Wi-Fi + Cellular':
        print('29400')
    else:
        print('Not Available')
main()
