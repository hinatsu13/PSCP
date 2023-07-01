'''Password'''
import hashlib
def main():
    '''Password'''
    sentance = input()
    bytee = sentance.encode('utf-8')
    mmm = hashlib.sha512()
    mmm.update(bytee)
    print(mmm.hexdigest().swapcase())
main()
