'''Duplicate I'''
def main():
    '''Duplicate I'''
    group_m = int(input())
    group_n = int(input())
    paper_member = []
    nani = []
    dont = []
    for _ in range(group_m + group_n):
        member = input()
        paper_member.append(member)
    for i in range(len(paper_member)):
        if paper_member[i] not in nani:
            nani.append(paper_member[i])
        else:
            dont.append(paper_member[i])
    if dont == []:
        print('Nope')
    else:
        dont.sort()
        dont.reverse()
        for i in dont:
            print(i)
main()
