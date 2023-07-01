'''BreakPassword'''
def pas(num):
    '''Password'''
    import hashlib
    num = '%05d' %num
    code = hashlib.sha512()
    code.update(num.encode('utf-8'))
    return code.hexdigest().lower()

def de_cd():
    '''BreakPassword'''
    code = input().lower()
    for i in range(0, 100000):
        password = i
        if pas(password) == code:
            break
    print('%05d' %password)
de_cd()
