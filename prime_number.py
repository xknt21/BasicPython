import numpy as np
a = 61
b = 10

# TODO


def is_prime_number(i):
    #２かどうか確かめる
    if i == 2:
        return True
    #偶数かどうか確かめる（これでほぼ1/2の確率で判定が終わる）
    if i % 2 == 0:
        return False
    
    till = np.sqrt(i)  #平方根
    j = 3
    while j <= till:
        if i % j == 0:  #iがjで割り切れたら
            return False
        j = j + 2   #次に大きい奇数に変えておく
    return True

print('61 is a prime number?', is_prime_number(a))
print('10 is a prime number?', is_prime_number(b))

# 素数かどうか求めたい数の平方根よりも小さな素数までで割り切れるかどうか調べたらそれ以上は必要ない