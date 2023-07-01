'''Turnstile'''
def main():
    '''Turnstile'''
    paper = ''
    ans = 0
    while True:
        word = input()
        paper += word
        if word == 'END':
            break
    for i in range(len(paper)):
        if paper[i] == 'C' and paper[i + 1] == 'P':
            ans += 1
        else:
            pass
    print(ans)
main()
