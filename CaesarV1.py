'''CaesarV1'''
def main():
    '''CaesarV1'''
    # แม่งเอ้ยยยยยยยยยยยยยยยยยยยยยยยยยยย
    import string
    a_z = string.ascii_lowercase
    distances = int(input())
    sentance = input()
    paper = ''
    for i in sentance:
        if i.isupper():
            idx = a_z.upper().find(i)
            paper += a_z[(idx + distances) % 26].upper()
        elif i.islower():
            idx = a_z.find(i)
            paper += a_z[(idx + distances) % 26]
        else:
            paper += i
    print(paper)
main()
