a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def euclid(a, b):
    if a < b:
        a, b = b, a

    remain = a % b

    if remain == 0:
        return b
    else:
        return euclid(b, remain)

print(euclid(a, b)) 

def is_mutually_prime(a, b):
    gcm = euclid(a, b)

    if gcm == 1:
        return True
    else:
        return False
    
print(is_mutually_prime(a, b))
