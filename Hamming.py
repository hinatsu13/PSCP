'''Hamming'''
def main():
    '''Hamming'''
    text1 = list(map(str, input()))
    text2 = list(map(str, input()))
    hamming = 0
    for i in range(max(len(text1), len(text2))):
        if text1[i] != text2[i]:
            hamming += 1
    print(hamming)
main()
