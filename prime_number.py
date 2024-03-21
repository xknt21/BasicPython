import numpy as np
a = 3.14
b = 10

# TODO


def is_prime_number(n):
    if not type(n) is int:
        print('正の整数を引数に指定してください')

    elif n <= 0:
        print('正の整数を引数に指定してください。')
 
    if n == 1:
        return False
    
    #２かどうか確かめる
    if n == 2:
        return True
    #偶数かどうか確かめる（これでほぼ1/2の確率で判定が終わる）
    if n % 2 == 0:
        return False
    
    till = np.sqrt(n)  #平方根
    j = 3
    while j <= till:
        if n % j == 0:  #iがjで割り切れたら
            return False
        j = j + 2   #次に大きい奇数に変えておく
    return True

print('61 is a prime number?', is_prime_number(a))
print('10 is a prime number?', is_prime_number(b))

# 素数かどうか求めたい数の平方根よりも小さな素数までで割り切れるかどうか調べたらそれ以上は必要ない