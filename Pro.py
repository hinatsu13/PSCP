'''Pro'''
def main():
    '''Pro'''
    pro_come = int(input())
    pro_pay = int(input())
    price = int(input())
    custom = int(input())
    outpro = custom % pro_come
    inpro = ((custom - outpro) // pro_come) * (price * pro_pay)
    print((outpro * price) + inpro)
main()
