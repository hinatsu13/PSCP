'''Safe'''
def main(password, start):
    '''Safe'''
    paper_pass = []
    paper_start = []
    forward = 0
    backward = 0
    rotate = 0
    for i in password:
        paper_pass.append(ord(i))
    for j in start:
        paper_start.append(ord(j))
    for char in range(len(password)):
        forward = abs(paper_pass[char] - paper_start[char])
        backward = 26 - abs(paper_pass[char] - paper_start[char])
        if forward <= backward:
            rotate += forward
        else:
            rotate += backward
    print(rotate)
main(input(), input())
