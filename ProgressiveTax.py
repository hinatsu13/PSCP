'''ProgressiveTax'''
def taxes(income):
    '''tax another'''
    tax = 0
    if income > 500000:
        if income > 750000:
            tax += 250000 * (15 / 100)
        else:
            tax += (income - 500000) * (15 / 100)
    if income > 750000:
        if income > 1000000:
            tax += 250000 * (20 / 100)
        else:
            tax += (income - 750000) * (20 / 100)
    if income > 1000000:
        if income > 2000000:
            tax += 1000000 * (25 / 100)
        else:
            tax += (income - 1000000) * (25 / 100)
    if income > 2000000:
        if income > 4000000:
            tax += 2000000 * (30 / 100)
        else:
            tax += (income - 2000000) * (30 / 100)
    return tax

def main():
    '''ProgressiveTax'''
    income = int(input())
    tax = 0
    if income < 150001:
        tax += 0
    if income > 150000:
        if income > 300000:
            tax += 150000 * (5 / 100)
        else:
            tax += (income - 150000) * (5 / 100)
    if income > 300000:
        if income > 500000:
            tax += 200000 * (10 / 100)
        else:
            tax += (income - 300000) * (10 / 100)
    if income > 500000:
        tax += taxes(income)
    if income > 4000000:
        tax += (income - 4000000) * (35 / 100)
    print(int(tax))
main()
