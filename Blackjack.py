'''Blackjack'''
def main():
    '''find how much number in my hand'''
    many_card = int(input())
    summ = 0
    paper = []
    for _ in range(many_card):
        card = input()
        paper += card
        if card == "J" or card == "Q" or card == "K":
            summ += 10
        elif card == "A":
            pass
        else:
            summ += int(card)
    if "A" in paper:
        if "10" or "J" or "Q" or "K":
            summ += 11
        else:
            summ += 1
    for _ in range(paper.count("A") - 1):
        if paper.count("A") > 1:
            summ += 1
    if "A" in paper and summ > 21:
        summ -= 10
    print(summ)
main()
